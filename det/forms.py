from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput
from .models import Expense,Profile
from datetime import date


# - Create/Register a user (Model Form)
class SigninForm(UserCreationForm):
	email = forms.EmailField(required=True)
	class Meta:

		model = User
		fields = ['username', 'email', 'password1', 'password2']

# - Authentication a user (Model Form)

class LoginForm(AuthenticationForm):

	username = forms.CharField(widget=TextInput())
	password = forms.CharField(widget=PasswordInput())

class UserUpdateForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['first_name','last_name','phone']

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['expense_title', 'category', 'amount', 'date', 'description']
        
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'max': str(date.today())}),
        }
