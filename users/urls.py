from django.urls import path
from users import views

app_name = 'users'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('', views.homeredirect, name='homeredirect'),
    path('logout/', views.logout_view, name='logout'),
    path('addmoney/', views.addmoney, name='addmoney'),
    path('mybookings/', views.mybookings, name='mybookings'),
    path('addevent/', views.organizer_addevent, name='addevent'),
    path('eventdetails/<int:event_id>', views.organizer_eventdetails, name='eventdetails')
]