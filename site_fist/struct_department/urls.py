from django.urls import path
from .views import *

app_name = 'struct'
urlpatterns = [
    path('struct/', start_home_page, name='home'),
]