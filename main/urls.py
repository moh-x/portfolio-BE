from django.urls import path
from .views import ProfileApiView


app_name = 'main'

urlpatterns = [
    path('profile/<int:pk>/', ProfileApiView.as_view(), name='profile'),
]
