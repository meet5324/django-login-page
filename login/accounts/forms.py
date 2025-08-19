from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.exceptions import ValidationError

class RegistrationForm(forms.ModelForm):
    user_id = forms.CharField(label="User ID", max_length=150)
    designation = forms.CharField(max_length=100, required=False)
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]

    def clean_user_id(self):
        username = self.cleaned_data["user_id"]
        if User.objects.filter(username__iexact=username).exists():
            raise ValidationError("This user ID is already taken.")
        return username

    def clean_email(self):
        email = (self.cleaned_data.get("email") or "").strip().lower()
        if User.objects.filter(email__iexact=email).exists():
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
        user = User(
            username=self.cleaned_data["user_id"],
            first_name=self.cleaned_data["first_name"],
            last_name=self.cleaned_data["last_name"],
            email=self.cleaned_data["email"],
        )
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
            # Ensure Profile exists and update designation
            from .models import Profile
            profile, created = Profile.objects.get_or_create(user=user)
            profile.designation = self.cleaned_data.get("designation", "")
            profile.save()
        return user


class EmailAuthenticationForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        self.user_cache = None
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned = super().clean()
        email = (cleaned.get("email") or "").strip().lower()
        password = cleaned.get("password")

        if email and password:
            try:
                user_obj = User.objects.get(email__iexact=email)
            except User.DoesNotExist:
                raise ValidationError("Invalid email or password.")

            user = authenticate(username=user_obj.username, password=password)
            if user is None:
                raise ValidationError("Invalid email or password.")
            if not user.is_active:
                raise ValidationError("This account is inactive.")
            self.user_cache = user
        return cleaned

    def get_user(self):
        return self.user_cache
