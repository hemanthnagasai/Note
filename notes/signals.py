from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.utils.timezone import now
from .models import Profile

@receiver(user_logged_in)
def update_login_time(sender, request, user, **kwargs):
    profile, created = Profile.objects.get_or_create(user=user)
    profile.last_login_time = now()

    if not profile.has_logged_in_before:
        profile.has_logged_in_before = True
    profile.save()
