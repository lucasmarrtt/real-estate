from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('lista-de-propriedades/', views.property_list, name='lista-de-propriedades'),
    path('detalhes-do-imovel/<slug:slug>', views.property_detail, name='detalhes-do-imovel'),
]