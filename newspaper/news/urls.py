from django.urls import path
from .views import index, details

urlpatterns = [
    path('news/', index, name='index'),
    path('news/<int:pk>', details, name='details'),

]