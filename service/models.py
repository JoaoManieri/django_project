from django.db import models


class Categoria(models.Model):
    name = models.CharField(max_length=100)
    dt_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Parts(models.Model):
    date = models.DateTimeField()
    descript = models.CharField(max_length= 300)
    valor = models.DecimalField(max_digits=7, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Parts"

    def __str__(self):
        return self.descript