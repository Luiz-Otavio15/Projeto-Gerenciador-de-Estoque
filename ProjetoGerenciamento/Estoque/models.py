from django.db import models

# Create your models here.

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='foto/')
    estoque = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def delete(self, *args, **kwargs):
        self.ativo = False
        self.save()
    


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)  # usado no soft delete

    class Meta:
        abstract = True