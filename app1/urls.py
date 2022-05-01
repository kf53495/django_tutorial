from django.urls import path

from .views import IndexView

urlpatterns = [
    path('', IndexView.as_view()), #中身が空のクオテーションでトップページを表す
]