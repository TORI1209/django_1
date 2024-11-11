from django.urls import path
from .views import IndexView, ProfileView, TableMakeView, process_form  # process_formを追加

urlpatterns = [
    path('', IndexView.as_view(), name='index'),  # ビューに名前を付けるのが推奨
    path('profile/', ProfileView.as_view(), name='profile'),
    path('table_make/', TableMakeView.as_view(), name='table_make'),
    path('process_form/', process_form, name='process_form'),  # 関数ベースビューのパス
]
    # path('news/<str:info.title>/', InformationView.as_view()),


