from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from notes.models import Note
from notes.utils import send_emailjs_reminder
from datetime import date

class Command(BaseCommand):
    help = "Send reminder email to users who haven't written a note today"

    def handle(self, *args, **kwargs):
        users = User.objects.all()
        today = date.today()

        for user in users:
            note_exists = Note.objects.filter(user=user, date=today).exists()
            if not note_exists:
                send_emailjs_reminder(user.email, user.username)
                self.stdout.write(f"Sent reminder to {user.email}")
