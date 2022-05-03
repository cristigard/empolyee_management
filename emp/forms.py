from django import forms
from .models import Employee,Group, Membership, Files, Role
from django.core.exceptions import ValidationError



#calendar picker for filds
class DateInput(forms.DateInput):
    input_type = 'date'


class FilesForm(forms.ModelForm):
    class Meta:
        model = Files
        fields = ['file_name', 'file' ]
        widgets = {
                'file_name': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'e.g. Contract de munca, Act aditional...'
                })}

    # def clean_file(self):
    #     file = self.cleaned_data['file']
    #     if not file.name.endswith('.pdf'):
    #         raise ValidationError("Please upload only '.pdf' files")
    #     return file.name.title()
    


class MembershipForm(forms.ModelForm):
    class Meta:
        model = Membership
        fields = ['group','date_joined']
        widgets = {
            'date_joined': DateInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                }),
            'employee': forms.Select(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                }),
             'group': forms.Select(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                })
            }
            

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name','email', 'employment_date' , 'cim', 'role', 'manager',]
        widgets = {
            'employment_date': DateInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                }),
            'manager': forms.Select(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                }),
             'role': forms.Select(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                }),
            'first_name': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'First Name'
                }),
            'email': forms.EmailInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Email'
                }),
            'last_name': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Last Name'
                }),
            'cim': forms.NumberInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Contract individual munca'
                })
            }
    
    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        return first_name.title()

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        return last_name.title()

        

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = [ 'name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                }),}

    def clean_name(self):
        name= self.cleaned_data['name']
        return name.title()


class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = [ 'name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                }),}

    def clean_name(self):
        name= self.cleaned_data['name']
        return name.title()