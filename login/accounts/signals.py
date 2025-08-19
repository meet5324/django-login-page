# accounts/signals.py
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    from .models import Profile
    if created:
        # Only create if not exists, don't overwrite designation
        Profile.objects.get_or_create(user=instance)
