from django.db import models
from django.contrib.auth.models import User
from django.db.models import CASCADE
from django.utils import timezone

# from location_field.models.plain import PlainLocationField

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200, null=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Customer(models.Model):
    user = models.OneToOneField(User,
                                null=True,
                                blank=True,
                                on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=15, null=True)
    email = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=255, default='New Delhi')
    # location = PlainLocationField(based_fields=['city'], zoom=7, null=True)
    profile_pic = models.ImageField(default="profile1.jpg",
                                    null=True,
                                    blank=True)

    def __str__(self):
        return self.name


class Vendor(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=15, null=True)
    email = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=255, default='New Delhi')
    # location = PlainLocationField(based_fields=['city'], zoom=7, null=True)
    profile_pic = models.ImageField(default="profile1.jpg",
                                    null=True,
                                    blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    quantity = models.FloatField(null=True)
    category = models.ForeignKey(Category,
                                 null=True,
                                 on_delete=models.SET_NULL)
    is_new = models.BooleanField(default=True)
    product_pic = models.ImageField(default="profile1.jpg",
                                    null=True,
                                    blank=True)
    created = models.DateTimeField(default=timezone.now)
    vendor = models.ForeignKey(Vendor, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ProductComment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    author = models.CharField(max_length=200, null=True)
    content = models.TextField()
    created = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.product.name