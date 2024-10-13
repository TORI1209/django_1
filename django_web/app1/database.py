import os
import sqlite3

# 現在のディレクトリ（スクリプトと同じ場所）を取得
current_dir = os.path.dirname(__file__)

# データベースファイルのパスを指定
db_path = os.path.join(current_dir, 'database.db')

# データベースに接続
conn = sqlite3.connect(db_path)

# カーソルを作成
cur = conn.cursor()

# テーブルを作成
cur.execute('''
CREATE TABLE IF NOT EXISTS information (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date STRING,
    title STRING,
    context STRING
)
''')

# コミットして変更を保存
conn.commit()

# カーソルと接続を閉じる
cur.close()
conn.close()
