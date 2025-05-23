from django.urls import path
from .views import user_register, user_login, user_logout

urlpatterns = [
    path("logout/", user_logout, name="logout"),
    path("login/", user_login, name="login"),
    path("register/", user_register, name="register"),
]
