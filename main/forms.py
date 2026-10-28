from django import forms 
from .models import  Product 

class ProductForm(forms.ModelForm):
    name = forms.CharField(max_length=100,
                           label='Name product',
                           widget= forms.TextInput(attrs={'class':'create_form',
                                                          'placeholder': 'Smoke 30ml Cherry'}))
    price = forms.DecimalField(max_digits=10, 
                               decimal_places=2,
                               label = 'Price your product',
                               widget=forms.NumberInput(attrs={'class': 'create_form',
                                                               'placeholder': '349.56'}))
    description = forms.CharField(max_length=2000,
                                  label = 'description',
                                  widget=forms.Textarea(attrs={'class': 'create_form',
                                                               'placeholder': 'Sweet cherry flavor liquid.'}))
    photo = forms.ImageField(label='Photo',
                             widget= forms.FileInput(attrs={'class': 'create_form'}))
    stock = forms.IntegerField(min_value=0,
                               label='Quantity in stock',
                               widget=forms.NumberInput(attrs={'class':'create_form',
                                                               'placeholder':'34'}))
    top_product = forms.BooleanField(required=False,
                                     label='Top product',
                                     widget=forms.CheckboxInput(attrs={'class':'create_form'}))

    
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'photo', 'stock', 'top_product']
        

class DeviceForm(ProductForm):
    power = forms.IntegerField(required=True,
                               label='Power',
                               widget=forms.NumberInput(attrs={'class':'create_form',
                                                               'placeholder':'30'}))
    color = forms.CharField(required=True,
                            max_length=100,
                            label='Color',
                            widget=forms.TextInput(attrs={'class':'create_form',
                                                          'placeholder':'Red'}))
    battery_capacity = forms.IntegerField(required=True,
                                          label='Battery capacity',
                                          widget=forms.NumberInput(attrs={'class':'create_form',
                                                                          'placeholder':'1200'}))
    guarantii = forms.DecimalField(required=True,
                                   label='Guarantee',
                                   widget=forms.NumberInput(attrs={'class':'create_form',
                                                                   'placeholder':'12'}))


    class Meta(ProductForm.Meta):
        fields = ['name', 'price', 'description', 'photo', 'stock', 'top_product',
                  'power', 'color', 'battery_capacity', 'guarantee']


class LiquidForm(ProductForm):
    volme_liquid = forms.IntegerField(required=True,
                                   label='Volume',
                                   widget=forms.NumberInput(attrs={'class':'create_form',
                                                                   'placeholder': '30'}))
    taste = forms.CharField(required=True,
                            label='Taste',
                            max_length=100,
                            widget=forms.TextInput(attrs={'class':'create_form'}))
    nicitine_capacity = forms.IntegerField(required=True,
                                           label='Nicotin capacity',
                                           widget=forms.NumberInput(attrs={'class':'create_form',
                                                                           'placeholder':'50'}))


    class Meta(ProductForm.Meta):
        fields = ['name', 'price', 'description', 'photo', 'stock', 'top_product',
                  'volme_liquid', 'taste', 'nicotine_capacity']


class CartridgeForm(ProductForm):
    volme_cartridge = forms.DecimalField(required=True,
                                         label='Volume',
                                         widget=forms.NumberInput(attrs={'class':'create_form',
                                                                         'placeholder':'30'}))
    resistance = forms.DecimalField(required=True, 
                                    label='Resistance',
                                    widget=forms.NumberInput(attrs={'class':'create_form',
                                                                    'placeholder':'0.2'}))
    compatibility = forms.CharField(max_length=120,
                                    required=True,
                                    label='Compatibility',
                                    widget=forms.TextInput(attrs={'class':'create_form',
                                                                  'placeholder':'Xros, Xslim'}))


    class Meta(ProductForm.Meta):
        fields = ['name', 'price', 'description', 'photo', 'stock', 'top_product',
                  'volume_cartridge', 'resistance', 'compatibility']
        
                
        