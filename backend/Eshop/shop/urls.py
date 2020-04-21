"""Eshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from .views import *

urlpatterns = [
    path('', TemplateView.as_view(template_name='shop/index.html'), name='index'),
    path('categories/', TemplateView.as_view(template_name='shop/categories.html'), name='categories'),
    path('product-page/', ProductPageView.as_view(), name='product-page'),
    path('shopping-cart/', TemplateView.as_view(template_name='shop/shopping-cart.html'), name='shopping-cart'),
    path('check-out/', TemplateView.as_view(template_name='shop/check-out.html'), name='check-out'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('404/', TemplateView.as_view(template_name='shop/404.html'), name='404'),
]
