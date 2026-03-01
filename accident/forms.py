from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=150, required=True)
    last_name = forms.CharField(max_length=150, required=True)

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2",
        ]


class LoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)





from django import forms
from .models import AccidentReport

class AccidentReportForm(forms.ModelForm):
    class Meta:
        model = AccidentReport
        fields = ['vehicle_type', 'location', 'latitude', 'longitude', 'notes', 'image']
        widgets = {
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
        }
from django import forms
from .models import AccidentReport

class AccidentReportForm(forms.ModelForm):
    class Meta:
        model = AccidentReport
        fields = ['vehicle_type', 'location', 'latitude', 'longitude', 'notes', 'image']

        widgets = {
            'vehicle_type': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
            'notes': forms.Textarea(attrs={'class': 'form-control'}),
        }


class AccidentReportForm(forms.ModelForm):
    class Meta:
        model = AccidentReport
        fields = [
            'name',
            'mobile',
            'vehicle_number',
            'vehicle_type',
            'location',
            'latitude',
            'longitude',
            'notes',
            'image',
            'video'
        ]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control'}),
            'vehicle_number': forms.TextInput(attrs={'class': 'form-control'}),

            'vehicle_type': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'latitude': forms.NumberInput(attrs={'class': 'form-control'}),
            'longitude': forms.NumberInput(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control'}),
        }
