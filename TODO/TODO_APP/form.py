from django import forms

# creating a form
class InputForm(forms.Form):

	Username = forms.CharField(max_length = 200)
	Password = forms.CharField(widget = forms.PasswordInput())
	Confirm_password = forms.CharField(widget = forms.PasswordInput())
