from django.urls import path
from . import views

urlpatterns = [
    path('atualizar/<int:produto_id>/', views.atualizar_estoque, name='atualizar_estoque'),
    path('remover/<int:produto_id>/', views.remover_estoque, name='remover_estoque'),
]
