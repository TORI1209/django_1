from typing import Any
from django.views.generic import TemplateView

#　json の import
from django.shortcuts import render
import json
from django.http.response import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self):
        ctxt = super().get_context_data()
        #名前入力
        ctxt["username"] = ""   
        return ctxt
    
    def get_context_data(self):
        ctxt = super().get_context_data()
        with open("C:/Users/EDO-NET User/Desktop/django_1/django_web/app1/information.json","r") as json_read:
            json_data = json.load(json_read)
            ctxt["date"] = json_data["information"][0]["date"] 
            ctxt["title"] = json_data["information"][0]["title"] 
            ctxt["context"] = json_data["information"][0]["context"] 

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
    
