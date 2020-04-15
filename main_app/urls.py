from django.urls import path
from .views import home, on_off_for_check


urlpatterns = [
    path('', home),
    path('check/<int:pk>/', on_off_for_check, name='checking'),
]