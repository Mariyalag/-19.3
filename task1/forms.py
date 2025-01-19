from django import forms
class UserRegister(forms.Form):
    username = forms.CharField(max_length=30, required=True)
    password = forms.CharField(min_length=8, widget=forms.PasswordInput, required=True)
    repeat_password = forms.CharField(min_length=8, widget=forms.PasswordInput, required=True)
    age = forms.IntegerField(min_value=0, max_value=999, required=True)
