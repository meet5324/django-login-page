# DRF registration view
from rest_framework import generics
from .serializers import RegisterSerializer
from .models import CustomUser
from rest_framework.permissions import AllowAny

class RegisterAPIView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
class DeleteAccountView(LoginRequiredMixin, View):
    login_url = "login"
    def post(self, request):
        user = request.user
        logout(request)
        user.delete()
        messages.success(request, "Your account has been deleted.")
        return redirect(reverse_lazy("login"))
from django.contrib.auth import login, logout
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.views import View
from .forms import RegistrationForm, UsernameAuthenticationForm

# JWT imports
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

class RegisterView(View):
    template_name = "accounts/register.html"  # folder 'accounts'
    def get(self, request):
        return render(request, self.template_name, {"form": RegistrationForm()})
    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
                user = form.save()
                return redirect("login")
        return render(request, self.template_name, {"form": form})

class LoginView(View):
    template_name = "accounts/login.html"  # folder 'accounts'
    def get(self, request):
        if request.user.is_authenticated:
            return redirect("home")
        return render(request, self.template_name, {"form": UsernameAuthenticationForm()})

    def post(self, request):
        form = UsernameAuthenticationForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            if user:
                login(request, user)
                # Send login notification email
                send_mail(
                    subject="Login Notification",
                    message=f"User {user.username} has logged in.",
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[user.email],
                    fail_silently=True
                )
                return redirect("home")
        return render(request, self.template_name, {"form": form})
        return render(request, self.template_name, {"form": form})

class LogoutView(View):
    def post(self, request):
        logout(request)
        return redirect("login")

class HomeView(LoginRequiredMixin, View):
    template_name = "accounts/home.html"  # folder 'accounts'
    login_url = "login"
    def get(self, request):
        profile = None
        if hasattr(request.user, 'profile'):
            profile = request.user.profile
        return render(request, self.template_name, {"profile": profile})
