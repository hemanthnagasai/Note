from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('my-notes/', views.my_notes, name='my_notes'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add-note/', views.add_note, name='add_note'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
]
