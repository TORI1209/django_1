import sqlite3
import os

# 現在位置の取得
current_dir = os.path.dirname(__file__)
db_path = os.path.join(current_dir, 'database.db')


# データベース接続
conn = sqlite3.connect(db_path)
cur = conn.cursor()

# idの最大値を取得 max_idに収納 int
cur.execute('SELECT MAX(id) FROM information')
max_id = cur.fetchone()[0]

# 確認用
# print("max_id = ",max_id)


for i in range(1,max_id + 1):
    # データの取得（informationテーブルにid = 1のレコードがあるかを確認）
    cur.execute('SELECT * FROM information WHERE id = ?',(i,))

    # 結果を取得して表示
    row = cur.fetchone()

    print(row)
    # data_date = row[1]
    # print(data_date)


# カーソルと接続を閉じる
if cur:
    cur.close()
if conn:
    conn.close()
現在位置の取得


