from typing import Any
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self):
        ctxt = super().get_context_data()
        #名前入力
        ctxt["username"] = ""   
        return ctxt

class HelpView(TemplateView):
    template_name = "help_index.html"

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
