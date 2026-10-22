from django.urls import path
from . import views

app_name = 'booking'

urlpatterns = [
    path('', views.events_index, name="events_index"),
    path('<int:event_id>/book',views.events_book, name="events_book"),
    path('book/successpage', views.booking_success, name="booking_success")
]