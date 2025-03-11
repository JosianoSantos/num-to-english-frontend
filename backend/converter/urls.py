from django.urls import path
from .views import ConvertNumberView

urlpatterns = [
    path('num_to_english', ConvertNumberView.as_view(), name='num_to_english'),
]
