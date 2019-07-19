from django.conf.urls import url
from . import views
from django.urls import path

app_name = "users"

urlpatterns = [
    url('login/', views.login_view, name="login"),
    url('register/', views.register_view, name="register"),
    url('logout/', views.logout_view, name="logout"),
    url('account_update_form/', views.account_view, name='account_update_form'),

]