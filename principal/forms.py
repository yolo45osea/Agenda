from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#-----------------------------------------------------------------------------------------------------

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(RegistroForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    

#-----------------------------------------------------------------------------------------------------

class CustomPasswordResetForm(forms.Form):
    email = forms.EmailField(label="Correo electrónico", max_length=254)