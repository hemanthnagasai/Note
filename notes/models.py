from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.utils.timezone import now, localdate
from datetime import timedelta

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=500)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.date}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    real_name = models.CharField(max_length=100, blank=True, null=True)
    image = models.ImageField(upload_to='profile_images/', default='default.jpg')
    has_logged_in_before = models.BooleanField(default=False)
    last_login_time = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return f"{self.user.username}'s Profile"

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    real_name = models.CharField(max_length=100, blank=True)
    has_logged_in_before = models.BooleanField(default=False)
    last_login_time = models.DateTimeField(null=True, blank=True)
    streak = models.IntegerField(default=0)
    last_note_date = models.DateField(null=True, blank=True)

    def update_streak(self):
        today = localdate()
        if self.last_note_date is None:
            self.streak = 1
        elif self.last_note_date == today - timedelta(days=1):
            self.streak += 1
        elif self.last_note_date == today:
            pass  
        else:
            self.streak = 1  

        self.last_note_date = today
        self.save()
