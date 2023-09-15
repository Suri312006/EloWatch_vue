# yourapp/urls.py
from django.urls import path
from .api import your_anonymous_view

urlpatterns = [
    path('hi/', your_anonymous_view, name='token_authetication'),
    # Add more URL patterns as needed
]
