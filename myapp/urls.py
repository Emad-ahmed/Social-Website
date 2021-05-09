from django.urls import path
from myapp.views import HomeView, SignView, LoginView, user_logout, user_profile, user_change_password, UploadView
from django.contrib.auth import views as auth_views
from myapp.forms import MyPasswordResetForm, MysetPasswordForm

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('signup', SignView.as_view(), name='signup'),
    path('login', LoginView.as_view(), name='login'),
    path('upload', UploadView.as_view(), name='upload'),
    path('logout', user_logout, name='logout'),
    path('user_profile', user_profile, name='user_profile'),
    path('user_change_password', user_change_password,
         name='user_change_password'),

    path('password-reset/',
         auth_views.PasswordResetView.as_view(template_name='password_reset.html', form_class=MyPasswordResetForm), name='password_reset'),

    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),


    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html', form_class=MysetPasswordForm), name='password_reset_confirm'),

    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
]
