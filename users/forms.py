from cProfile import label
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, PasswordResetForm


#manage widget of form in PasswordReset
class CustomUserPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['email'].widget.attrs.update(
            {'class': "form-control",
                        'style': 'max-width: 300px;'}
            )


#manage widget of form in PasswordChange
class CustomUserPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['old_password'].widget.attrs.update(
            {'class': "form-control",
                        'style': 'max-width: 300px;'}
            )
        self.fields['new_password1'].widget.attrs.update(
            {'class': "form-control",
                        'style': 'max-width: 300px;'}
            )
        self.fields['new_password2'].widget.attrs.update(
            {'class': "form-control",
                        'style': 'max-width: 300px;'}
            )

#manage widget of form in LoginView
class CustomLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update(
        {'class': "form-control",
                    'style': 'max-width: 300px;'}
        )
        self.fields['password'].widget.attrs.update(
        {'class': "form-control",
                    'style': 'max-width: 300px;'}
        )


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;'
                }))
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;'
                }))

    class Meta:
        model = CustomUser
        fields = ('email', 'username')
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                }),
            'username': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                }),
            }

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = CustomUser
        fields = ['image', 'email', 'username']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['image', 'email', 'username']
        widgets = {
             'image': forms.FileInput(attrs={

                }),
            'email': forms.EmailInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px; ',
                }),
            'username': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                }),
            }



