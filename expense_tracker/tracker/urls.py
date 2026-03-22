from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

path('',views.Home,name='Home'),


 path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
   
path('register/',views.registration,name='register'),
path('logout/',views.logout_view,name='logout'),

path('add-expense/',views.add_expense,name='add_expense'),
path('add-income/',views.add_income,name='add_income'),
path('delete-expense/<int:id>/',views.delete_expense,name='delete_expense')]