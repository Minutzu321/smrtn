from django import forms

class LoginForm(forms.Form):
    nume = forms.CharField(label='Numele de utilizator', max_length=100)
    parola = forms.CharField(label='Parola', max_length=100, widget=forms.PasswordInput())