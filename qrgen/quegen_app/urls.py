from django.urls import path
from .views import openai_view
urlpatterns = [
    path('', openai_view),
]