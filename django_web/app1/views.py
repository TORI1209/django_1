from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"

class HelpView(TemplateView):
    template_name = "help_index.html"