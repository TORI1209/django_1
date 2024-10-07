from typing import Any
from django.views.generic import TemplateView

#相対パス用
import os 

#json の import
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

class InformationView(TemplateView):
    template_name = "information.html"

    
