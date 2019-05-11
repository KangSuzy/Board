from board import views
from django.contrib import admin
from django.urls import path



urlpatterns = [
    path('post/', views.post, name='post'),
    path('show/', views.show, name='show'),
    path('main/', views.main, name='main'),
    path('<int:board_id>/', views.detail, name='detail'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/delete', views.delete, name='delete'),

]