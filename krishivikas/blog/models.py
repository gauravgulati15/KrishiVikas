from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="blog/", blank=True, null=True)
    category = models.ForeignKey("Category",
                                 null=True,
                                 on_delete=models.SET_NULL)
    created = models.DateTimeField(default=timezone.now)
    tags = TaggableManager(blank=True)

    class Meta:
        verbose_name = "post"
        verbose_name_plural = "posts"

    def __str__(self):
        return self.title


class Category(models.Model):
    category_name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"

    def __str__(self):
        return self.category_name


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.CharField(max_length=200, null=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.post.title