from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime

app = Flask(__name__)

# 資料庫初始化
def init_db():
    conn = sqlite3.connect('appointments.db')
    cursor = conn.cursor()

    # 創建預約表格，添加名字和電話欄位
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS appointments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            date TEXT NOT NULL,
            time TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

# 初始化資料庫
init_db()

# 首頁路由
@app.route('/')
def index():
    return render_template('total_times.html')

# 提交預約表單的路由
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name', '')
    phone = request.form.get('phone', '')
    date = request.form.get('date', '')
    time = request.form.get('time', '')

    # 將預約存入資料庫
    conn = sqlite3.connect('appointments.db')
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO 'appointments' (`name`, `phone`, `date`, `time`) VALUES (?, ?, ?, ?)",
                   (name, phone, date, time))

    conn.commit()
    conn.close()

    return f'已預約時間: {date} {time}'

if __name__ == '__main__':
    app.run(debug=True)
