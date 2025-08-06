from django.db import models


class Category( models.Model ):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    def __str__( self ):
        return self.name
    

class Product( models.Model ): 
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to="products/images/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products'
    )

    def __str__( self ):
        return self.name
