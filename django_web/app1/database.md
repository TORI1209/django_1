# データベース使い方

## 1,sqlite3 を import
```python
import sqlite3
```

## 2,データベースに接続

```python
dbname = 'ファイル名.db'
conn = sqlite3.connect(dbname)
```
db_path = '/path/to/your/database.db'でパスの指定も行える


## 3,わからんとりあえず書く
```python
cur = conn.cursor()
```
## 4,実行
### テーブル新規作成
```python
cur.execute(
'CREATE TABLE persons(カラム名 INTEGER PRIMARY KEY AUTOINCREMENT, カラム名 STRING)')
```
(例ではpersonsテーブルを作成)  

形式を指定:INTEGER数字 STRING文字

PRIMARY KEY = id はかぶっっちゃだめよってこと

AUTOINCREMENT = 連番で勝手にidを作ってくれるということ

### テーブルに要素を追加
```python
cur.execute('INSERT INTO テーブル名(カラム名) values("新規登録する要素")') 
```


### テーブルのデータを更新・削除
データ更新（例ではカラム「name」の「Takahashi」を「Tanaka」に変更します）
```python
cur.execute('UPDATE persons SET name = "Tanaka" WHERE name = "Takahashi"')
```

### データ削除（例ではカラム「name」の「Suzuki」を削除します）
```python
cur.execute('DELETE FROM persons WHERE name = "Suzuki"')
```

### テーブルのデータを取得
例では、personsテーブルデータを全件取得 * = すべて
```python
cur.execute('SELECT * FROM persons where id = 1')
```

### 取得したデータを出力
```python
for row in cur:
    print(row)
```


# 5.データベースに情報をコミット
```python
conn.commit()
```

# 6.データベースの接続を切断
```python
cur.close()
conn.close()
```