from django.urls import path
from . import views
urlpatterns = [
    path('bound/', views.bound, name='bound')
]