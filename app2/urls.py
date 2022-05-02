from django.urls import path, include

from .views import Index2View, About2View

urlpatterns = [
    path('', Index2View.as_view())
    path('about2/', About2View.as_view())
]