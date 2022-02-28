from tabnanny import verbose
from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self) -> str:
        return f"{self.name}"

    class Meta: 
        verbose_name_plural = "Categories"  #Changer name plural dans le tableau

class Product(models.Model):
    name= models.CharField("nom produit",max_length=100)
    age= models.IntegerField()
    description=models.TextField()
    price=models.FloatField(default=0)
    created_at=models.DateField(auto_now_add=True)
    category =models.ForeignKey(  #OneToMany
        Category,
        on_delete=models.CASCADE,
        null=True
    )

    def __str__(self) -> str:
        return f"{self.name}"