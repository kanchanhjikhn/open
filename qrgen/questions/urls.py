# urls.py
from django.urls import path
from .views import ,

urlpatterns = [
    path('', ask_question, name='ask_question'),
    path('answer/', answer_question, name='answer_question'),
]
