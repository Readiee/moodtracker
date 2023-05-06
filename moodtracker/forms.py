from django import forms
from .models import *


class UserForm(forms.ModelForm):
    password_confirm = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': "input-field", 'spellcheck': "false", 'required': False}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'login', 'password', 'password_confirm']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': "input-field", 'spellcheck': "false"}),
            'last_name': forms.TextInput(attrs={'class': "input-field", 'spellcheck': "false"}),
            'login': forms.TextInput(attrs={'class': "input-field", 'spellcheck': "false"}),
            'password': forms.PasswordInput(attrs={'class': "input-field", 'spellcheck': "false"})
        }

    def is_valid(self):
        if self.data.get('password_confirm', None) == self.data.get('password'):
            return self.is_bound and not self.errors
        return False


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'login']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': "input-field", 'spellcheck': "false"}),
            'last_name': forms.TextInput(attrs={'class': "input-field", 'spellcheck': "false"}),
            'login': forms.TextInput(attrs={'class': "input-field", 'spellcheck': "false"}),
        }


class TrackerForm(forms.ModelForm):
    class Meta:
        model = Tracker
        fields = ['image']

