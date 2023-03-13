from jinja1.views import *
from django.urls import path
app_name='hello'
urlpatterns = [
    path('specific_jinjatag/',specific_jinjatag,name='specific_jinjatag'),
]
