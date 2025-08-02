from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from accounts.models import Profile

User = get_user_model()

class MyUserCreationForm(UserCreationForm):
    birth_date = forms.DateField(
        required=False,
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='Дата рождения'
    )
    avatar = forms.ImageField(
        required=True,
        label='Аватар'
    )


    class Meta(UserCreationForm.Meta):
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=commit)
        return user