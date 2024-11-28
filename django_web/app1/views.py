from typing import Any
from django.views.generic import TemplateView

#相対パス用
import os 

# データベースのimport
import sqlite3
# from django.http import HttpResponse

#json の import
from django.shortcuts import render
import json
from django.http.response import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie

from django.http import HttpResponseRedirect

from django.shortcuts import render
from django.http import HttpResponse

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self):
        ctxt = super().get_context_data()
        #名前入力
        ctxt["username"] = ""   
        return ctxt
    
    def get_context_data(self):
        ctxt = super().get_context_data()

        current_dir = os.path.dirname(__file__)
        json_path = os.path.join(current_dir, "information.json")

        with open(json_path, "r") as json_read:
            json_data = json.load(json_read)

            # json の情報を context に格納
            ctxt["information_list"] = json_data["information"]
            ctxt["info_count"] = len(json_data["information"])
            # ctxt["date"] = json_data["information"][0]["date"] 
            # ctxt["title"] = json_data["information"][0]["title"] 
            # ctxt["context"] = json_data["information"][0]["context"] 

            id = 1

            return ctxt
            
    


class ProfileView(TemplateView):
    template_name = "profile_index.html"

    def get_context_data(self):
        ctxt = super().get_context_data()
        
        #取得スキル入力
        skills = ["python", "go"]
        #練習中スキル入力
        practice_skills = ["html", "css"]
        
        ctxt["num_skills"] = len(skills)
        ctxt["skills"] = skills
        
        ctxt["num_practice_skills"] = len(practice_skills)
        ctxt["practice_skills"] = practice_skills

        return ctxt



class TableMakeView(TemplateView):
    template_name = "table_make.html"

    print("テーブル名くらい2")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # データベースパスの設定
        current_dir = os.path.dirname(__file__)
        db_path = os.path.join(current_dir, 'database.db')

        # データベースに接続して情報を取得
        with sqlite3.connect(db_path) as conn:
            cur = conn.cursor()
            cur.execute('SELECT * FROM information WHERE id = 1')
            row = cur.fetchone()

        # テンプレートに渡すコンテキストを設定
        context["response_tables"] = row

        return context


    

    def get_context_data(self):

        # 現在位置の取得
        current_dir = os.path.dirname(__file__)
        db_path = os.path.join(current_dir, 'database.db')

        # データベース接続
        conn = sqlite3.connect(db_path)
        cur = conn.cursor()

        # idの最大値を取得 max_idに収納 int
        cur.execute('SELECT MAX(id) FROM information')
        max_id = cur.fetchone()[0]

        #変数に変数を入れるために必須
        varia = {}

        if max_id:  
            for i in range(1,max_id + 1):
                # データの取得（informationテーブルにid = 1のレコードがあるかを確認）
                cur.execute('SELECT * FROM information WHERE id = ?',(i,))

                # 結果を取得して表示
                row = cur.fetchone()  

                if row:
                    # 日付、タイトル、内容をそれぞれ
                    varia[f"{i}data_date"] = row[1]
                    varia[f"{i}data_title"] = row[2]      
                    varia[f"{i}data_context"] = row[3]
    
        context = varia
        conn.close()

        print("おちんぽぽ",context)

        return context



def process_form(request):
    if request.method == 'POST':
        # フォームからデータを取得
        database_date = request.POST.get('database_date')
        database_title = request.POST.get('database_title')
        data_context = request.POST.get('data_context')

        # データベースにデータを保存
        current_dir = os.path.dirname(__file__)
        db_path = os.path.join(current_dir, 'database.db')

        with sqlite3.connect(db_path) as conn:
            cur = conn.cursor()
            cur.execute(
                'INSERT INTO information (date, title, context) VALUES (?, ?, ?)',
                (database_date, database_title, data_context)
            )
            conn.commit()

        # データが保存されたらリダイレクト
        return HttpResponseRedirect('/success')  # 成功ページにリダイレクト

    return render(request, 'form_page.html')  # フォームページを表示



class SuccessView(TemplateView):  
    template_name = "table_make_success.html"

class Tablemake_cushion_View(TemplateView):
    template_name = "table_make_cushion.html"

class TableReMakeView(TemplateView):
    template_name = "table_remake.html"
