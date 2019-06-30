from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, label="Prénom")
    last_name = forms.CharField(max_length=30, required=False, label="Nom")
    email = forms.EmailField(max_length=254, label="Adresse mail")
    username = None

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2', )
