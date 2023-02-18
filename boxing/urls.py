from django.urls import path
from boxing import views

urlpatterns = [
    path('',views.Home,name="Home")
    

]
