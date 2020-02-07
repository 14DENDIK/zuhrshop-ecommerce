from django.db import models
from brands.models import Brand
from brands.models import NameField as LoweredField


class Product(models.Model):
    name = LoweredField(max_length=200)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    is_on_sale = models.BooleanField(default=False)
    on_sale_price = models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True)
    is_available = models.BooleanField(default=True)
    main_image = models.ImageField(upload_to="product-images", default='phone.jpg')

    class Category(models.TextChoices):
        PHONE = 'phone', 'Phone'
        ACCESSORY = 'accessory', 'Accessory'

    category = models.CharField(max_length=10, choices=Category.choices, default=Category.PHONE)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="product-images")


class Phone(Product):

    class Condition(models.TextChoices):
        NEW = 'new', 'NEW'
        USED = 'used', 'USED'

    condition = models.CharField(max_length=4, choices=Condition.choices, default=Condition.NEW)
    ram = models.IntegerField(default=1)
    memory = models.IntegerField(default=1)
    camera = models.IntegerField(default=1)
    screen_dimension = models.FloatField(default=1)
    screen = LoweredField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT)

    def __str__(self):
        return self.condition + '-' + self.name


class Accessory(Product):
    phone = models.ManyToManyField(Phone)
    material = LoweredField(max_length=200)

    def __str__(self):
        return self.name
