from django.urls import path
from django.urls import path

from . import views

urlpatterns = [
    path('', views.club, name='club'),
    path('login/', views.inlogin, name='login'),
    path('logout/', views.outlogin, name='logout'),
    path('atletas/', views.atletas, name='atletas'),
    path('atletas/<slug:atleta_slug>/', views.record, name='record'),
    path('logros/', views.logros, name='logros'),
    path('password/', views.password, name='password'),
    path('ficha/', views.ficha, name='ficha'),
    path('marcas/', views.marcas, name='marcas'),
]