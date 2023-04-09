from django.db import models
from user.models import UserModel
from product.models import ProductModel


# Create your models here.
class BoundModel(models.Model):
    class Meta:
        db_table = "bound"

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    code = models.ForeignKey(ProductModel, on_delete=models.CASCADE)
    bound_price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)