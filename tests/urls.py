from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('raw/', views.index_raw, name='index_raw'),
    path('bg-gray/', views.bg_gray, name='bg-gray'),
]