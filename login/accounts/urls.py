from django.urls import path
from .views import RegisterView, LoginView, LogoutView, HomeView, DeleteAccountView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/",    LoginView.as_view(),    name="login"),
    path("logout/",   LogoutView.as_view(),   name="logout"),
    path("delete-account/", DeleteAccountView.as_view(), name="delete_account"),
    path("", HomeView.as_view(), name="home"),
]
