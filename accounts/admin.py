from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import TutorCreationForm, TutorChangeForm
from .models import Tutor

class TutorAdmin(UserAdmin):
    add_form = TutorCreationForm
    form = TutorChangeForm
    model = Tutor
    list_display = ['username', 'email', 'classes', 'monday_start', 'monday_end', 'tuesday_start', 'tuesday_end', 'wednesday_start', 'wednesday_end', 'thursday_start', 'thursday_end', 'friday_start', 'friday_end']

admin.site.register(Tutor, TutorAdmin)