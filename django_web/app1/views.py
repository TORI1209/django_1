from typing import Any
from django.views.generic import TemplateView
import os  # 相対パス用
import sqlite3  # データベースの操作
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie
import urllib.parse


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **arg):
        context = super().get_context_data(**arg)

        # データベースパスの設定
        db_path = os.path.join(os.path.dirname(__file__), 'database.db')

        # データベース接続して情報を取得
        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            query = "SELECT date, title FROM information"
            cursor.execute(query)
            rows = cursor.fetchall()

        # コンテキストに渡す
        context["information_list"] = [{"date": row[0], "title": row[1]} for row in rows]
        return context


class ProfileView(TemplateView):
    template_name = "profile_index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # スキル情報
        skills = ["python", "go"]
        practice_skills = ["html", "css"]

        context["num_skills"] = len(skills)
        context["skills"] = skills
        context["num_practice_skills"] = len(practice_skills)
        context["practice_skills"] = practice_skills

        return context


class TableMakeView(TemplateView):
    template_name = "table_make.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # データベースパスの設定
        db_path = os.path.join(os.path.dirname(__file__), 'database.db')

        # データベース接続
        with sqlite3.connect(db_path) as conn:
            cur = conn.cursor()

            # id = 1 のレコードを取得
            cur.execute('SELECT * FROM information WHERE id = 1')
            row = cur.fetchone()
            context["response_table"] = row if row else "No data for id = 1"

            # id の最大値を取得
            cur.execute('SELECT MAX(id) FROM information')
            max_id = cur.fetchone()[0]

            # 複数のデータをコンテキストに追加
            if max_id:
                for i in range(1, max_id + 1):
                    cur.execute('SELECT * FROM information WHERE id = ?', (i,))
                    row = cur.fetchone()
                    if row:
                        context[f"{i}_data_date"] = row[1]
                        context[f"{i}_data_title"] = row[2]
                        context[f"{i}_data_context"] = row[3]

        return context


def process_form(request):
    if request.method == 'POST':
        # フォームからデータを取得
        database_date = request.POST.get('database_date')
        database_title = request.POST.get('database_title')
        data_context = request.POST.get('data_context')

        # データベースにデータを保存
        db_path = os.path.join(os.path.dirname(__file__), 'database.db')

        with sqlite3.connect(db_path) as conn:
            cur = conn.cursor()
            cur.execute(
                'INSERT INTO information (date, title, context) VALUES (?, ?, ?)',
                (database_date, database_title, data_context)
            )
            conn.commit()

        # 成功ページにリダイレクト
        return HttpResponseRedirect('/success')

    # フォームページを表示
    return render(request, 'form_page.html')


class SuccessView(TemplateView):
    template_name = "table_make_success.html"


class Tablemake_cushion_View(TemplateView):
    template_name = "table_make_cushion.html"


class TableReMakeView(TemplateView):
    template_name = "table_remake.html"



class InformationView(TemplateView):
    template_name = "information.html"

    def get_context_data(self, **arg):
        context = super().get_context_data(**arg)

        title = urllib.parse.unquote(self.kwargs.get('title'))
        print(f"test: {title}")

        db_path = os.path.join(os.path.dirname(__file__), 'database.db')

        with sqlite3.connect(db_path) as conn:
            cursor = conn.cursor()
            query = "SELECT date, title, context FROM information WHERE title = ?"
            cursor.execute(query, (title,))
            row = cursor.fetchone()

        if row:
            context["info"] = {
                "date": row[0],
                "title": row[1],
                "context": row[2],
            }
        else:
            context["info"] = {"error": "No data found for the given title."}

        return context
