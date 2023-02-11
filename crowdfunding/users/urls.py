from django.urls import path

from . import views

# to use the new user view add the urls

urlpatterns = [
    path('', views.CustomUserList.as_view(), name='customuser-list'),
    path('<int:pk>/', views.CustomUserDetailView.as_view(), name='customuser-detail'),
    path('change-password/', views.ChangePasswordView.as_view(), name='change_password')
]
