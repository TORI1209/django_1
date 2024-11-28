from typing import Any
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import sqlite3
import os


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

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

        # サンプルデータの追加
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

        # データベースからのデータ取得
        current_dir = os.path.dirname(__file__)
        db_path = os.path.join(current_dir, 'database.db')
        with sqlite3.connect(db_path) as conn:
            cur = conn.cursor()
            cur.execute('SELECT * FROM information WHERE id = 1')
            row = cur.fetchone()

        # テンプレートに渡す
        context["response_tables"] = row
        return context


class TableReMakeView(TemplateView):
    template_name = "table_remake.html"


class Tablemake_cushion_View(TemplateView):
    template_name = "table_make_cushion.html"


@csrf_exempt
def process_form(request):
    if request.method == 'POST':
        # データ取得
        database_date = request.POST.get('database_date')
        database_title = request.POST.get('database_title')
        data_context = request.POST.get('data_context')

        # データベースに保存
        current_dir = os.path.dirname(__file__)
        db_path = os.path.join(current_dir, 'database.db')
        with sqlite3.connect(db_path) as conn:
            cur = conn.cursor()
            cur.execute(
                'INSERT INTO information (date, title, context) VALUES (?, ?, ?)',
                (database_date, database_title, data_context)
            )
            conn.commit()

        return HttpResponseRedirect('/success')

    return render(request, 'form_page.html')


class SuccessView(TemplateView):
    template_name = "table_make_success.html"
