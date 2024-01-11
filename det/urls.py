from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('',views.homepage, name=""),
    path('register',views.register, name="register"),
    path('my-login',views.my_login, name="my login"),
    path('user-logout',views.user_logout, name="user-logout"),


    path('profile', views.profile, name='profile'),
    path('profile/update', views.profile_update, name='profile_update'),   
    path('change-password', views.change_password, name='change_password'),
    path('delete_account', views.delete_account, name='delete_account'),


    path('dashboard',views.dashboard, name="dashboard"),
    path('expense_list/<str:status>/', views.expense_list, name='expense_list'),
    path('add',views.add_expense, name="add_expense"),
    path('edit/<int:pk>/', views.edit_expense, name='edit_expense'),
    path('delete/<int:pk>/', views.delete_expense, name='delete_expense'),
    path('restore-expense/<int:pk>/', views.restore_expense, name='restore_expense'),
    path('permanently-delete-expense/<int:pk>/', views.permanently_delete_expense, name='permanently_delete_expense'),
]

