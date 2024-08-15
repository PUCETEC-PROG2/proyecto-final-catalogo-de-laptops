from django.db import models
from django.forms import ValidationError
from .validation import validar_cedula, validar_correo

class Client(models.Model):
    cedula = models.CharField(max_length=10, validators=[validar_cedula], null=False, unique=True)
    nombre = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=100, validators=[validar_correo], null=False)
    direccion = models.CharField(max_length=100, null=False)
    
    def clean(self):
        super().clean()
        if Client.objects.filter(cedula=self.cedula).exists():
            raise ValidationError({'cedula': 'Ya existe un cliente con esta cédula.'})
    
    def __str__(self) -> str:
        return f'{self.nombre}'

class Product(models.Model):
    procesador = models.CharField(max_length=10, null=False, unique=True)
    ram = models.CharField(max_length=45, null=False)
    modelo = models.CharField(max_length=45, null=False)
    disco = models.CharField(max_length=20, null=False)
    
    LAPTOP_CATEGORY = [
        ('Oficina', 'Oficina'),
        ('Gaming', 'Gaming'),
        ('Gama alta', 'Gama alta'),
        ('Gama media', 'Gama media'),
        ('Gama baja', 'Gama baja')
    ]
    
    category = models.CharField(max_length=45, choices=LAPTOP_CATEGORY, null=False)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    tamaño_pantalla = models.DecimalField(max_digits=10, decimal_places=2)
    descuento = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    imagen = models.ImageField(upload_to='laptops_images')  # Cambié el upload_to para que coincida con la aplicación actual
    voltaje = models.IntegerField()
    
    def __str__(self) -> str:
        return f'{self.ram} {self.modelo}'  # Cambié 'model' por 'modelo'

class Sale(models.Model):                                                
    client = models.ForeignKey(Client, on_delete=models.CASCADE)  # Cambio a ForeignKey a Client
    product = models.ForeignKey(Product, on_delete=models.CASCADE)  # Cambio a ForeignKey a Product
    total = models.DecimalField(max_digits=10, decimal_places=2)
    descuento = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
    
    def __str__(self) -> str:
        return f'{self.client.nombre} - {self.product.modelo}'  # Representación más clara de la venta
