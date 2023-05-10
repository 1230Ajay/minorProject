from django.db import models

# Create your models here.
class Contents(models.Model):
    
    title = models.CharField(max_length=200 , null=False , blank=False)
    payment = models.CharField(max_length=100)
    desc = models.TextField(max_length=500)
    description = models.CharField(null=True , max_length=200)
    paid = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title
