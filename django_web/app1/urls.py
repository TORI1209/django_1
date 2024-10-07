from django.urls import path

from .views import IndexView
from .views import ProfileView
from .views import InformationView

urlpatterns = [
    path('', IndexView.as_view()),
    path('profile/', ProfileView.as_view()),
    path('news/<str:info.title>/', InformationView.as_view()),
]
