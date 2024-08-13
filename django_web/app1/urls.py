from django.urls import path

from .views import IndexView
from .views import HelpView

urlpatterns = [
    path('', IndexView.as_view()),
    path('help/', HelpView.as_view()),
]
