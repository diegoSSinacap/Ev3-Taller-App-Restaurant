# Generated by Django 4.2.7 on 2023-11-27 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pedidos',
            fields=[
                ('id_pedido', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Platos',
            fields=[
                ('id_plato', models.AutoField(primary_key=True, serialize=False)),
                ('nom_plato', models.CharField(max_length=200)),
                ('desc_plato', models.CharField(max_length=255)),
                ('prec_plato', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id_user', models.AutoField(primary_key=True, serialize=False)),
                ('nom_usuario', models.CharField(max_length=200)),
                ('cre_usuario', models.DateTimeField()),
                ('pos_usuario', models.CharField(max_length=255)),
            ],
        ),
    ]
