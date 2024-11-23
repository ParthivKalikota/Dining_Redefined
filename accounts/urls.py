from django.urls import path
from . import views
urlpatterns = [
    path('signup_page',views.signup_page,name = "signup_page"),
    path('login_page',views.login_page,name = "login_page"),
    path('logout',views.logout,name='logout'),
    
]