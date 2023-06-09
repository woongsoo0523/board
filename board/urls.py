from django.urls import path 
from . import views

app_name='board'

urlpatterns = [
    path('', views.index,name="index"),
    path('list/', views.list,name='list'),
    path('add/', views.add, name="add"),
    path('detail/<int:id>/', views.detail, name="detail"),
    path('delete/<int:id>/', views.delete, name="delete"),
    path('update/<int:id>/', views.update, name="update"),
    
]