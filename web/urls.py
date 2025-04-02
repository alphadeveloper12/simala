from django.urls import path
from .views import *  # Import the view

urlpatterns = [path('', index, name='index'),  # This maps the home ('/') route to index view
  path("submit-contact/", submit_contact, name="submit_contact"), ]
