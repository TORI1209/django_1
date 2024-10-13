from django.urls import path

from .views import IndexView, ProfileView, TableMakeView

urlpatterns = [
    path('', IndexView.as_view()),
    path('profile/', ProfileView.as_view()),
    path('table_make/', TableMakeView.as_view()),
    # path('news/<str:info.title>/', InformationView.as_view()),
]
