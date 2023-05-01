from django.urls import path
from .views import *

urlpatterns = [
    path('login',Login.as_view(),name='Login View URL Pattern'),
    path('register',Register.as_view(),name='Register View URL Pattern')
]