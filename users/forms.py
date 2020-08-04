from django import forms


class LoginForm(forms.Form):

    email = forms.EmailField()
    passwod = forms.CharField(widget=forms.PasswordInput)
