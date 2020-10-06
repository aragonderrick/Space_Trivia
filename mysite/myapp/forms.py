from django import forms
from django.core.validators import validate_slug
from . import models

def must_be_caps(value):
    if not value.isupper():
        raise forms.ValidationError("Not all uppercase")
    #Always return to the cleaned data, wether you have changed it or not
    return value

def must_be_bob(value):
    if not value.startswith("BOB"):
        raise forms.ValidationError("Must start with BOB")
    return value

class SuggestionForm(forms.Form):
    suggestion = forms.CharField(
        label='Suggestion',
        required=True,
        max_length=240,
        validators=[validate_slug, must_be_caps, must_be_bob],
    )

    def save(self):
        suggestion_instance = models.suggestionModel()
        suggestion_instance.suggestion = self.cleaned_data["suggestion"]
        suggestion_instance.save()
        return suggestion_instance