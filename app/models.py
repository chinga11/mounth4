from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField(default=0)
    def  __str__(self):
        return self.title