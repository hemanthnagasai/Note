from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Note, Profile
from .forms import NoteForm
from datetime import date
from django.contrib import messages
from django.contrib.auth import login
from .forms import RegisterForm
from django.utils.timezone import now
from .forms import ProfileForm



@login_required
def home(request):
    today = date.today()
    note = Note.objects.filter(user=request.user, date=today).first()

    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            new_note = form.save(commit=False)
            new_note.user = request.user
            new_note.date = today
            new_note.save()
            request.user.profile.update_streak()
            messages.success(request, "Your note for today was saved.")
            return redirect('my_notes')
    else:
        form = NoteForm(instance=note)

    return render(request, 'notes/home.html', {'form': form, 'today': today})


@login_required
def add_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            new_note = form.save(commit=False)
            new_note.user = request.user
            new_note.date = date.today()
            new_note.save()
            request.user.profile.update_streak()
            messages.success(request, "New note added successfully.")
            return redirect('my_notes')
    else:
        form = NoteForm()

    return render(request, 'notes/home.html', {'form': form, 'today': date.today()})  # reuse same template


@login_required
def my_notes(request):
    notes = Note.objects.filter(user=request.user).order_by('-date')
    return render(request, 'notes/my_notes.html', {'notes': notes})


@login_required
def dashboard(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    notes = Note.objects.filter(user=request.user)
    note_count = notes.count()
    note_count = Note.objects.filter(user=request.user).count()

    if profile.has_logged_in_before:
        messages.success(request, f"Welcome back, {request.user.username}!")
    else:
        messages.info(request, f"Welcome to your dashboard, {request.user.username}!")
        profile.has_logged_in_before = True
        profile.save()
    return render(request, 'notes/dashboard.html', {
        'notes': notes,
        'note_count': note_count,
        'last_login': profile.last_login_time,
        'streak': profile.streak,
    })


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            messages.success(request, "Account created successfully. Please log in.")
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def edit_profile(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)  
        if form.is_valid():
            form.save()

            new_email = form.cleaned_data.get('email')
            if new_email:
                request.user.email = new_email
                request.user.save()

            messages.success(request, 'Profile updated successfully.')
            return redirect('dashboard')
    else:
        form = ProfileForm(instance=profile)
        form.fields['email'].initial = request.user.email

    return render(request, 'notes/edit_profile.html', {'form': form})
