from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import LoginForm

app_name = 'accounts'
urlpatterns = [
    path('register/',views.register,name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html',redirect_authenticated_user=True, authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='account/logout',next_page ="/"), name='logout'),
    path('sign_up',views.sign_up,name='deconnection')
]
