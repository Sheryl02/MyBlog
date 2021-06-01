from django.urls import path
from .views import userRegister, changePasswords, viewProfile, userEditProfile, createAccount, editProfile
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('register/', userRegister.as_view(), name='register'),
    path('edit-settings/', userEditProfile.as_view(), name='edit-settings'),

    path('<int:pk>/profile/', viewProfile.as_view(), name='profile'),
    path('<int:pk>/edit-profile', editProfile.as_view(), name='edit-profile'),
    path('create-account', createAccount.as_view(), name='create-account'),

    # path('password/', auth_views.PasswordChangeView.as_view(template_name='registration/change_password.html')),
    path('password/', changePasswords.as_view(template_name='registration/change_password.html'), name='password'),
    path('password_success', views.password_success, name = 'password_success'),

]
