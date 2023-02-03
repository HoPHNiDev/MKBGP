from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticlesHome.as_view(), name='news'),
    path('<str:slug>', views.ArticlesView.as_view(), name='news_view'),
]
