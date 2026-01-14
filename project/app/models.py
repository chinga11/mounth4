from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    def  __str__(self):
        return self.title

class Post(models.Model):
    photo = models.ImageField(blank=True, null=True, upload_to="product/")
    title = models.CharField(max_length=200)
    text = models.TextField(blank=True)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    
    def  __str__(self):
        return self.title