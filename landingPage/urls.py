from django.urls import path
from .views import landing_page

urlpatterns = [
    path('', landing_page, name='home'),
    # Add other URL patterns as needed
]