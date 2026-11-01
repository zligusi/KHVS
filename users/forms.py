from django import forms
from .models import CustomUser 


class CustomUserLoginForm(forms.ModelForm):
    username = forms.CharField(required=True,
                               max_length=120,
                               label="Enter email",
                               widget=forms.TextInput(attrs={'class':'login_form',
                                                             'placeholder':'Grozniy@gmail.com'}))
    password = forms.CharField(required=True,
                               max_length=100, 
                               label='Enter password',
                               widget=forms.PasswordInput(attrs={'class':'login_form',
                                                                 }))

    class Meta():
        model = CustomUser
        fields = ['username', 'password']


class CustomUserRegisterForm(forms.ModelForm):
    usernsme = forms.CharField(required=True,
                               max_length=120,
                               label="Enter email",
                               widget=forms.TextInput(attrs={'class':'register_form',
                                                             'placeholder':'Grozniy@gmail.com'}))
    password1 = forms.CharField(required=True,
                               max_length=100, 
                               label='Enter password',
                               widget=forms.PasswordInput(attrs={'class':'register_form',
                                                                 }))
    password1 = forms.CharField(required=True,
                               max_length=100, 
                               label='Confir password',
                               widget=forms.PasswordInput(attrs={'class':'register_form',
                                                                 }))
    first_name = forms.CharField(required=True,
                                 max_length=25,
                                 label='Enter first name',
                                 widget=forms.TextInput(attrs={'class':'register_form',
                                                               'placeholder':'Roman'}))
    last_name = forms.CharField(required=True, 
                                max_length=25,
                                label= 'Enter last name',
                                widget=forms.TextInput(attrs={'class':'register_form',
                                                              'placeholder': 'Zolochev'}))
    date_of_birth = forms.DateField(required=False,
                                    label='Enter date of birth',
                                    widget=forms.DateInput(attrs={'class':'register_form'}))
    city = forms.CharField(required=False,
                           max_length=100,
                           label='Enter city',
                           widget=forms.TextInput(attrs={'class':'register_form',
                                                         'placeholder': 'Kyiv'}))
    postal_code = forms.IntegerField(required=False,
                                     label='Enter postal code',
                                     widget=forms.NumberInput(attrs={'class':'register_form',
                                                                     'placeholder': '61110'}))
    address_1 = forms.CharField(required=False,
                                label='Enter address',
                                widget=forms.TextInput(attrs={'class':'register_form', 
                                                             'placeholder':'street Morozova 11 '}))