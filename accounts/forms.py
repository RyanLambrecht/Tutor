from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Tutor

class TutorCreationForm(UserCreationForm):
    monday_start = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}), required=False)
    monday_end = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}), required=False)
    tuesday_start = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}), required=False)
    tuesday_end = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}), required=False)
    wednesday_start = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}), required=False)
    wednesday_end = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}), required=False)
    thursday_start = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}), required=False)
    thursday_end = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}), required=False)
    friday_start = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}), required=False)
    friday_end = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}), required=False)

    class Meta:
        model = Tutor
        fields = [
            'username', 'first_name', 'last_name', 'email', 'password1', 'password2',
            'classes', 'monday_start', 'monday_end', 'tuesday_start', 'tuesday_end',
            'wednesday_start', 'wednesday_end', 'thursday_start', 'thursday_end',
            'friday_start', 'friday_end'
        ]

class TutorChangeForm(UserChangeForm):
    monday_start = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}), required=False)
    monday_end = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}), required=False)
    tuesday_start = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}), required=False)
    tuesday_end = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}), required=False)
    wednesday_start = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}), required=False)
    wednesday_end = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}), required=False)
    thursday_start = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}), required=False)
    thursday_end = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}), required=False)
    friday_start = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}), required=False)
    friday_end = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}), required=False)

    class Meta:
        model = Tutor
        fields = ['classes', 'monday_start', 'monday_end', 'tuesday_start', 'tuesday_end',
                  'wednesday_start', 'wednesday_end', 'thursday_start', 'thursday_end',
                  'friday_start', 'friday_end']