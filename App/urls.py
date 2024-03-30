from . import views
from django.urls import path

urlpatterns = [
    path('', views.ExperimentList.as_view(), name="home"),
    path('<int:pk>/', views.DetailView.as_view(), name="experiment_detail")  
]
