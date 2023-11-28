from django.db import models

# Create your models here.
#class Usuarios(models.Model):
#    id_user = models.AutoField(primary_key=True)
#    nom_usuario = models.CharField(max_length=200)
#    cre_usuario = models.DateTimeField()
#    pos_usuario = models.CharField(max_length=255)

class Plato(models.Model):
    id = models.AutoField(primary_key=True)
    nom_plato = models.CharField(max_length=200)
    desc_plato = models.CharField(max_length=255)
    prec_plato = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Pedidos(models.Model):
    id = models.AutoField(primary_key=True)
    nom_plato = models.ForeignKey("sistema.Plato", on_delete=models.CASCADE,)
    desc_pedido = models.CharField(max_length=255)
    pedido_estado = models.BooleanField()
    def __str__(self):
        return self.name
