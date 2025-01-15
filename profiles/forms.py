from django import forms


class ProfileForm(forms.Form):
    # Antes:
    # user_image = forms.FileField()
    user_image = forms.ImageField()
