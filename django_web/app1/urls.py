from django.urls import path
from .views import (
    IndexView, ProfileView, TableMakeView, TableReMakeView,
    process_form, SuccessView, Tablemake_cushion_View, InformationView
)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('tablemake_cushion/', Tablemake_cushion_View.as_view(), name='tablemake_cushion'),
    path('tablemake_cushion/table_make/', TableMakeView.as_view(), name='table_make'),
    path('tablemake_cushion/table_remake/', TableReMakeView.as_view(), name='table_remake'),
    path('process_form/', process_form, name='process_form'),
    path('success/', SuccessView.as_view(), name='success'),
    path('news/<path:title>/', InformationView.as_view(), name='news'),
]
