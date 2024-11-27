"""blogproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from . import views

app_name = 'blogapp'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),  # トップページ（インデックス）
    path('game_list/', views.game_list, name='game_list'),  # ゲーム一覧ページ
    path('create/', views.game_create, name='game_create'),  # ゲーム登録ページ
    path('delete/<int:pk>/', views.game_delete, name='game_delete'),
    path('delete_bulk/', views.game_delete_bulk, name='game_delete_bulk'),  
]
