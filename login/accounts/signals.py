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
            # Send registration email to user's email address
            from django.core.mail import send_mail
            if instance.email:
                subject = 'Welcome to Our Site'
                message = f'Hello {instance.username},\n\nThank you for registering. You can now log in to your account.'
                from_email = 'meetsavaliya5324@gmail.com'
                recipient_list = [instance.email]
                send_mail(subject, message, from_email, recipient_list, fail_silently=True)
