from django.urls import path
from . import views


urlpatterns = [
    path('reg/', views.registerView, name='register_url'),
    path('log/', views.loginView, name='login_url'),
    path('lot/', views.logoutView, name='logot_url')
    
]