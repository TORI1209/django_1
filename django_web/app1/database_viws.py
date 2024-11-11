import sqlite3
import os

# 現在位置の取得
current_dir = os.path.dirname(__file__)
db_path = os.path.join(current_dir, 'database.db')

try:
    # データベース接続
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    # データの取得（personsテーブルにid = 1のレコードがあるかを確認）
    cur.execute('SELECT * FROM persons WHERE id = 1')

    # 結果を取得して表示
    row = cur.fetchone()  # 一件のみ取得
    if row:
        print(row)
    else:
        print("id=1 のレコードは見つかりませんでした。")

except sqlite3.Error as e:
    print(f"データベースエラーが発生しました: {e}")

finally:
    # カーソルと接続を閉じる
    if cur:
        cur.close()
    if conn:
        conn.close()