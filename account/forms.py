from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, min_length=3)
    password = forms.CharField(max_length=150, min_length=5)


class EditProfileForm(forms.Form):
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    email = forms.EmailField(max_length=150)


class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(max_length=150, min_length=5)
    new_password1 = forms.CharField(max_length=150, min_length=5)
    new_password2 = forms.CharField(max_length=150, min_length=5)

