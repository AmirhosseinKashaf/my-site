from django.urls import path, include
from accounts.views import *

app_name = 'accounts'

urlpatterns = [
    path('login',login_view,name='login'),
    path('logout',logout_view,name='logout'),
    path('signup',signup_view,name='signup'),
    path('forgot-password/',forgot_password_view, name='forgot_password'),
    path('reset-password/',reset_password_view, name='reset_password'),
    path('password-reset-complete/',password_reset_complete_view, name='password_reset_complete'),

]