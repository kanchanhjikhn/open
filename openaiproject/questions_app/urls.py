from django.urls import path
from .views import ask_question, ask_topic

urlpatterns = [
    path('', ask_topic, name='ask_topic'),
    path('ask/', ask_question, name='ask_question'),
]