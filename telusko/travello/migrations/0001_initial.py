
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombreCiudad', models.CharField(max_length=100)),
                ('descripcionCiudad', models.TextField()),
                ('imagenCiudad', models.ImageField(upload_to='pics')),
                ('precioTour', models.IntegerField()),
                ('ofertaTour', models.BooleanField(default=False)),
            ],
        ),
    ]
