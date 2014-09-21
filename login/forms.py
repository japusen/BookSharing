from django import forms
from login.models import UserInfo

class LoginForm(forms.ModelForm):
	error_css_class = 'has-error'
	umail = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'id': 'inputUmail', 'placeholder': 'Umail', 'autofocus'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'inputPassword', 'placeholder': 'Password'}))