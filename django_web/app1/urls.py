from django.urls import path

from .views import IndexView
from .views import ProfileView

urlpatterns = [
    path('', IndexView.as_view()),
    path('profile/', ProfileView.as_view()),
]
