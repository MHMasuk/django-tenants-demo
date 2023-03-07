from django.db import models


class ProductType(models.Model):
    product_type = models.CharField(max_length=256)

    def __str__(self):
        return self.product_type
