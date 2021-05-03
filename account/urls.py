from django.urls import path

from account import views

urlpatterns = [
    path('', views.index),
    path('login/', views.login_view),
    path('register/', views.register_view),
    path('dashboard/', views.dashboard),
    path('logout/', views.logout_view),
    path('dashboard/edit/', views.profile),
    path('dashboard/changepassword/', views.change_password)
]