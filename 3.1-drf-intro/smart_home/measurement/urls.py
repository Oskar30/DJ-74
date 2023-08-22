from django.urls import path
from . import views

urlpatterns = [
    path('sensors/', views.TempViewList.as_view()),
    path('sensors/<pk>/', views.OneSensorVieweUpdate.as_view()),
    path('measurements/', views.AddMeasurements.as_view()),
    ]
