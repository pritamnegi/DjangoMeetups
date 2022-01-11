from django import forms
from django.db import models
from django.db.models import fields

class RegistrationForm(forms.Form):
    email = forms.EmailField(label='Your email')