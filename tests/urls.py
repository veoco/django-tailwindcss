from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('bg-gray/', views.bg_gray, name='bg-gray'),
]