from django.db import models
from base.models import BaseModel
from django.utils.text import slugify
# Create your models here.

class  Category(BaseModel):
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    category_image = models.ImageField(upload_to="categories")

    def save( self, *args, **kwargs):
        self.slug = slugify( self.category_name )
        super(Category , self).save( *args , **kwargs )

    def __str__(self) -> str:
        return self.category_name


class ColorVarient(BaseModel):
    color_name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)

    def __str__(self) -> str :
        return self.color_name

class SizeVarient(BaseModel):
    size_name = models.CharField(max_length=100) 
    price = models.IntegerField(default=0)

    def __str__(self) -> str:   # method in Python is used to define a human-readable 
        return self.size_name   # string representation of an object when it's printed or logged.

class Product(BaseModel):
    product_name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="product")
    price = models.IntegerField()
    product_description = models.TextField()
    color_varients = models.ManyToManyField(ColorVarient, blank=True)
    size_varients = models.ManyToManyField(SizeVarient, blank=True)


    def save( self, *args, **kwargs):
        self.slug = slugify( self.product_name )
        super(Product , self).save( *args , **kwargs )

    def __str__(self) -> str:
        return self.product_name
    
    def get_product_price_by_size(self, size):
        return self.price+SizeVarient.objects.get(size_name = size).price
  

class ProductImage(BaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_images")
    image =  models.ImageField(upload_to="product")
