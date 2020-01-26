from django.urls import path

from .views import buttons_home_view

urlpatterns = [
    path('', buttons_home_view, name='button_home')
]