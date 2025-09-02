from django.urls import path
from .views import RegisterView, LoginView, LogoutView, HomeView, DeleteAccountView, RegisterAPIView

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("api/register/", RegisterAPIView.as_view(), name="api_register"),
    path("login/",    LoginView.as_view(),    name="login"),
    path("logout/",   LogoutView.as_view(),   name="logout"),
    path("delete-account/", DeleteAccountView.as_view(), name="delete_account"),
    path("", HomeView.as_view(), name="home"),
    # JWT endpoints
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
