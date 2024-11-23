from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name = 'home'),
    path('sample_page',views.sample_page,name="sample_page"),
    path('restaurant_page_Builder',views.restaurant_page_Builder,name='restaurant_page_Builder'),
    # path('signup_page',views.signup_page,name = "signup_page"),
    # path('login_page',views.login_page,name = "login_page"),
    # path('login.html#',views.login_page,name="login_page")
]