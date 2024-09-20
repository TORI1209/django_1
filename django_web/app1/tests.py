from django.test import TestCase

# Create your tests here.


#json test
import requests
import json


url = "http://127.0.0.1:8000/jsontest/"
sess = requests.session()

print(sess.get(url))

csrftoken = sess.cookies['csrftoken']

# ヘッダ
headers = {'Content-type': 'application/json',  "X-CSRFToken": csrftoken}

# 送信データ
prm = {"param1": "パラメータ１", "param2": "パラメータ２"}

# JSON変換
params = json.dumps(prm)

# POST送信
res = sess.post(url, data=params, headers=headers)

# 戻り値を表示
print(json.loads(res.text))
