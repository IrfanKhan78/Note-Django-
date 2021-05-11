from django.urls import path

from . import views

app_name = 'note'

urlpatterns = [
    path('home/', views.home, name = 'home'),
    path('detail/<int:cid>/', views.detail, name = 'detail'),
    path('add/', views.add, name = 'add'),
    path('trash', views.trash, name = 'trash'),
    path('delete/<int:cid>/', views.delete, name = 'delete'),
    path('clear/', views.clear, name = 'clear'),

]