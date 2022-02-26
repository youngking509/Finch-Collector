from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('finch/', views.finch_index, name='index'),
    path('finch/<int:finch_id>/', views.finch_detail, name='detail'),
    path('finch/create/', views.FinchCreate.as_view(), name='finch_create'),
    path('Finch/<int:pk>/update/', views.FinchUpdate.as_view(), name='finch_update'),
    path('Finch/<int:pk>/delete/', views.FinchDelete.as_view(), name='finch_delete'),
]


    