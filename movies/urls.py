from django.urls import path
from .views import *


app_name = 'movies'
urlpatterns = [
    path('', index, name='index'),
    path('<int:movie_id>', detail, name="detail"),

]
