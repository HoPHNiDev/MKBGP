from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductsHome.as_view(), name='products'),
    path('<str:slug>', views.ProductsView.as_view(), name='products_view'),
]
