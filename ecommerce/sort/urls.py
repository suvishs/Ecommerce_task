from django.urls import path
from . import views

urlpatterns = [
    path('sort_high_to_low/sort', views.sort_high_to_low, name='sort_high_to_low'),
    path('sort_low_to_high/sort',views.sort_low_to_high, name='sort_low_to_high'),

]