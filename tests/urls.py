from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('bg-gray/', views.bg_gray, name='bg-gray'),
    path('bg-gray-raw/', views.bg_gray_raw, name='bg-gray-raw'),
    path('tpl-bg-slate/', views.tpl_bg_slate, name='tpl-bg-slate'),
]