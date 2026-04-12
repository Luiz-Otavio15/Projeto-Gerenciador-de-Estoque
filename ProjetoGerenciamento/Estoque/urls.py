from django.contrib import admin
from django.urls import path

from Estoque import views


urlpatterns = [
    path('', views.tela_gerenciamento, name='tela_gerenciamento'),
    path('adicionar/', views.tela_adicionar, name='tela_adicionar'),
    path('editar/<int:id>/', views.tela_editar, name='tela_editar')
]