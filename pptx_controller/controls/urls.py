from django.urls import path
from controls import views

urlpatterns = [
    path('<str:key>/', views.press_key),
]
