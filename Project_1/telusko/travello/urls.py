from django.urls import path

from . import views


urlpatterns = [
    path('',views.index, name='index'),
    # path('getlocationdet',views.getlocationdet, name='getlocationdet'),
    path('getspecificlocation', views.getspecificlocation, name="/getspecificlocation")
]