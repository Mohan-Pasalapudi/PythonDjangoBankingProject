from django import forms
from .models import Admin,Employee,AccountHolder


class DateInput(forms.DateInput):
    input_type = "date"


class AdminLoginForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = "__all__"
        widgets = {"password":forms.PasswordInput()}


class EmployeeRegistrationForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
        widgets = {"dateofbirth":DateInput(),"password":forms.PasswordInput(),'fullname': forms.TextInput(attrs={'placeholder': 'Enter Full Name'}),'email': forms.TextInput(attrs={'placeholder': 'Enter Email Address'})}


class AccountHolderRegistrationForm(forms.ModelForm):
    class Meta:
        model = AccountHolder
        fields = "__all__"
        exclude = ['account_no']
        widgets = {"dateofbirth":DateInput(),"password":forms.PasswordInput(),'fullname': forms.TextInput(attrs={'placeholder': 'Enter Full Name'}),'email': forms.TextInput(attrs={'placeholder': 'Enter Email Address'})}


class TransferForm(forms.Form):
    sender_account = forms.ModelChoiceField(queryset=AccountHolder.objects.all(), label='From Account')
    receiver_account = forms.ModelChoiceField(queryset=AccountHolder.objects.all(), label='To Account')
    amount = forms.DecimalField(max_digits=10, decimal_places=2)
