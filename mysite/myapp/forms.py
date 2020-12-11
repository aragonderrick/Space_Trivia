from django import forms
from django.core.validators import validate_slug
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from . import models

def must_be_uniqiue(value):
    user = User.objects.filter(email=value)
    if len(user) > 0:
        raise forms.ValidationError("Email Already in Use")
    return value

class SuggestionForm(forms.Form):
    suggestion = forms.CharField(
        label='Suggestion',
        required=True,
        max_length=240,
    )

    def save(self, request):
        suggestion_instance = models.suggestionModel()
        suggestion_instance.suggestion = self.cleaned_data["suggestion"]
        suggestion_instance.client = request.user#user object from database
        suggestion_instance.save()
        return suggestion_instance

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(
        label="Email",
        required = True,
        validators=[must_be_uniqiue],
    )

    class Meta: 
        model = User
        fields = ("username", "email","password1", "password2")

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
            models.Profile.objects.create(user=user)
        return user