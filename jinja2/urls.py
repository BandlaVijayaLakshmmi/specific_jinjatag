from jinja2.views import *
from django.urls import path
app_name='hello'
urlpatterns = [
    path('specific_jinjatag2/',specific_jinjatag2,name='specific_jinjatag2'),
]
