from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    birth_date = forms.DateField(
        help_text='必須: YYYY-MM-DD 形式で入力して下さい。',
        label='誕生日',
    )

    class Meta:
        model = User
        fields = ('username', 'birth_date', 'password1', 'password2', )