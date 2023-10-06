
from django.urls import path
from qrcode_app import views
urlpatterns = [
    path('', views.index)
]