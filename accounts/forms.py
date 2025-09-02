
from django import forms
from django.core.exceptions import ValidationError
from .models import CustomUser
from django.contrib.auth import authenticate

class RegistrationForm(forms.ModelForm):
    username = forms.CharField(label="Username", max_length=150)
    designation = forms.CharField(max_length=100, required=False)
    phone_number = forms.CharField(label="Phone Number", max_length=20, required=True)
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = CustomUser
        fields = ["first_name", "last_name", "email", "username"]

    def clean_username(self):
        username = self.cleaned_data["username"]
        if CustomUser.objects.filter(username__iexact=username).exists():
            raise ValidationError("This username is already taken.")
        return username

    def clean_email(self):
        email = (self.cleaned_data.get("email") or "").strip().lower()
        if CustomUser.objects.filter(email__iexact=email).exists():
            raise ValidationError("An account with this email already exists.")
        return email

    def clean(self):
        cleaned = super().clean()
        p1 = cleaned.get("password")
        p2 = cleaned.get("password_confirm")
        if p1 and p2 and p1 != p2:
            self.add_error("password_confirm", "Passwords do not match.")
        return cleaned

    def save(self, commit=True):
        user = CustomUser(
            username=self.cleaned_data["username"],
            first_name=self.cleaned_data["first_name"],
            last_name=self.cleaned_data["last_name"],
            email=self.cleaned_data["email"],
        )
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
            # Ensure Profile exists and update designation and phone_number
            from .models import Profile
            profile, created = Profile.objects.get_or_create(user=user)
            profile.designation = self.cleaned_data.get("designation", "")
            profile.phone_number = self.cleaned_data.get("phone_number", "")
            profile.save()
        return user


class UsernameAuthenticationForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        self.user_cache = None
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned = super().clean()
        username = cleaned.get("username")
        password = cleaned.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise ValidationError("Invalid username or password.")
            if not user.is_active:
                raise ValidationError("This account is inactive.")
            self.user_cache = user
        return cleaned

    def get_user(self):
        return self.user_cache
