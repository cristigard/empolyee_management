from django.urls import path
from . import views 
from django.contrib.auth import views as auth_views
from .forms import CustomUserPasswordResetForm


urlpatterns = [
    
    path('', views.UserLoginView.as_view(), name = 'login'),
    path('user/signup/', views.UserSignUpView.as_view(), name = 'signup'),
    path('user/logout/', views.UserLogoutView.as_view(), name = 'logout'),
    path('user/profile/', views.profile, name = 'profile'),
    path('user/password_change/', views.UserChangePassView.as_view(), name = 'password_change'),
    path('user/password_change_done/', views.UserChangePassDoneView.as_view(), name = 'password_change_done'),

     path('user/password_reset/',
         auth_views.PasswordResetView.as_view(
             form_class = CustomUserPasswordResetForm,
             template_name='users/password_reset.html'
         ),
         name='password_reset'),
    path('user/password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='users/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('user/password_reset_confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='users/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('user/password_reset_complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='users/password_reset_complete.html'
         ),
         name='password_reset_complete'),
]