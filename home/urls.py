from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('detalhes-do-imovel/<slug:slug>', views.detalhes_do_imovel, name='detalhes-do-imovel'),
]