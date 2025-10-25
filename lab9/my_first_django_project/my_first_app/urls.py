from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.hello_world, name='hello_default'),
    path('hello/<str:name>/', views.hello_world, name='hello'),
    path('redirect/', views.my_redirect, name='redirect'),
    path('json/', views.json, name='json'),
    path('cookies/', views.show_cookies, name='cookies'),
]
