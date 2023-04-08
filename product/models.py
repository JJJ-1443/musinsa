from django.db import models
from user.models import UserModel


# Create your models here.
class ProductModel(models.Model):
    class Meta:
        db_table = "product"

    seller = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    code = models.CharField(max_length=256)
    prod_name = models.CharField(max_length=256)
    desc = models.CharField(max_length=256)
    price = models.IntegerField()
    sizes = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('F', 'Free'),
    )
    size = models.CharField(choices=sizes, max_length=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)