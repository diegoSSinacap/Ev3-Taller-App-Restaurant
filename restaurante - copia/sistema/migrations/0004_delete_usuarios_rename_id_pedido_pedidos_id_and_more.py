# Generated by Django 4.2.5 on 2023-11-27 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0003_rename_id_plato_plato_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Usuarios',
        ),
        migrations.RenameField(
            model_name='pedidos',
            old_name='id_pedido',
            new_name='id',
        ),
        migrations.AddField(
            model_name='pedidos',
            name='desc_pedido',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pedidos',
            name='pedido_estado',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]