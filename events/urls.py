from django.urls import path
from .views import *
urlpatterns = [
     path('all_events/',AllEventsView.as_view(),name = 'To Get All events'),
     path('create_event',CreateEventView.as_view(),name = 'To Create Events'),
     path('user_events/',UserEvents.as_view(),name = 'To Get All User Events'),
]

