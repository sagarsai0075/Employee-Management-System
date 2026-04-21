from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone
from .models import Employee
import re


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter full name',
                'required': True,
                'minlength': 2,
                'maxlength': 100
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter email address',
                'required': True
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter phone number (10-15 digits)',
                'required': True,
                'pattern': r'^[0-9\-\+\s\(\)]{10,15}$'
            }),
            'salary': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter salary',
                'required': True,
                'min': 0,
                'step': 0.01
            }),
            'joining_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'required': True
            }),
            'address': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter address',
                'required': True,
                'rows': 3,
                'maxlength': 500
            }),
            'department': forms.Select(attrs={
                'class': 'form-select',
                'required': True
            })
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if name and len(name.strip()) < 2:
            raise ValidationError('Name must be at least 2 characters long.')
        if name and not re.match(r'^[a-zA-Z\s\-\.\']+$', name):
            raise ValidationError('Name can only contain letters, spaces, hyphens, dots, and apostrophes.')
        return name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if email:
            # Check if email already exists
            existing = Employee.objects.filter(email=email).exclude(pk=self.instance.pk)
            if existing.exists():
                raise ValidationError('This email address is already registered.')
        return email

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        if phone:
            # Remove non-digit characters for validation
            phone_digits = re.sub(r'\D', '', phone)
            if len(phone_digits) < 10:
                raise ValidationError('Phone number must have at least 10 digits.')
            if len(phone_digits) > 15:
                raise ValidationError('Phone number cannot exceed 15 digits.')
        return phone

    def clean_salary(self):
        salary = self.cleaned_data.get('salary')
        if salary is not None:
            if salary < 0:
                raise ValidationError('Salary cannot be negative.')
            if salary > 9999999.99:
                raise ValidationError('Salary value is too high.')
        return salary

    def clean_joining_date(self):
        joining_date = self.cleaned_data.get('joining_date')
        if joining_date:
            if joining_date > timezone.now().date():
                raise ValidationError('Joining date cannot be in the future.')
        return joining_date

    def clean_address(self):
        address = self.cleaned_data.get('address')
        if address and len(address.strip()) < 5:
            raise ValidationError('Address must be at least 5 characters long.')
        return address