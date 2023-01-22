from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

from django import forms
from captcha.fields import CaptchaField

class CustomUserCreationForm(UserCreationForm, forms.ModelForm):
	class Meta(UserCreationForm):
		model = CustomUser
		fields = ('first_name', 'last_name', 'username', 'email',)

class CustomUserChangeForm(UserChangeForm):
	class Meta:
		model = CustomUser
		fields = ('profile_pic', 'first_name', 'last_name', 'bio', 'email',)