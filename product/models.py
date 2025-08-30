from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator, FileExtensionValidator
from cloudinary.models import CloudinaryField

from product.validators import Validate_File_Size



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
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products'
    )

    class Meta:
        ordering = ['id']

    def __str__( self ):
        return self.name
    

class Product_Images( models.Model ):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='images',
    )
    image = CloudinaryField('image')
    # image = models.ImageField(upload_to="products/images/", default="products/images/default_product_image.jpg", validators=[Validate_File_Size])
    # file = models.FileField(upload_to="product/files/", validators=[FileExtensionValidator(['pdf'])])


class Review( models.Model ):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    ratings = models.PositiveIntegerField( validators=[MinValueValidator(1), MaxValueValidator(5)] )
    comment = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"Review by {self.user.first_name} {self.user.last_name} on {self.product.name}"