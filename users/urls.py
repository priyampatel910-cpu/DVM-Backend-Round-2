from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('', views.homeredirect, name='homeredirect'),
    path('logout/', views.logout_view, name='logout')
]