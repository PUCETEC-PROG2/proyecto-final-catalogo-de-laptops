from django import forms 

from .models import Client, Product, Sale

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        widgets = {
            'cedula': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'})
        }

class SaleForm(forms.ModelForm):                                          
    class Meta:                                                             
        model = Sale                                                      
        fields = '__all__'                                                  
        widgets = {                                                         
            'client': forms.Select(attrs={'class': 'form-control'}),     
            'product': forms.Select(attrs={'class': 'form-control'}),       
	    'total': forms.TextInput(attrs={'class': 'form-control'}),      
 	    'date': forms.TextInput(attrs={'class': 'form-control'})     
        }                                                                   
          
        
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'procesador': forms.TextInput(attrs={'class': 'form-control'}),
            'ram': forms.TextInput(attrs={'class': 'form-control'}),
            'model': forms.TextInput(attrs={'class': 'form-control'}),
            'disco': forms.TextInput(attrs={'class': 'form-control'}),
            'procesador': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'tamaño pantalla': forms.NumberInput(attrs={'class': 'form-control'}),
            'descuento': forms.NumberInput(attrs={'class': 'form-control'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'voltaje': forms.NumberInput(attrs={'class': 'form-control'})
        }
#Para agregar stock si un producto ya existe :p
class ProductStockForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['procesador', 'voltaje']  
