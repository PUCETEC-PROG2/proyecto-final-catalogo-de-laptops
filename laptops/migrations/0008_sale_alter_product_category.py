# Generated by Django 4.2 on 2024-08-13 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laptops', '0007_alter_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.CharField(max_length=45)),
                ('product', models.CharField(choices=[('Guitarras Electro Acusticas', 'Guitarras Electro Acusticas'), ('Guitarras Electricas', 'Guitarras Electricas'), ('Guitarras Clasicas', 'Guitarras Clasicas'), ('Bajos', 'Bajos'), ('Guitarras Acusticas', 'Guitarras Acusticas')], max_length=45)),
                ('total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount', models.DecimalField(decimal_places=2, default=0.0, max_digits=5)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Guitarras Electro Acusticas', 'Guitarras Electro Acusticas'), ('Guitarras Electricas', 'Guitarras Electricas'), ('Guitarras Clasicas', 'Guitarras Clasicas'), ('Bajos', 'Bajos'), ('Guitarras Acusticas', 'Guitarras Acusticas')], max_length=45),
        ),
    ]
