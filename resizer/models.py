from django.db import models

# Create your models here.
class Image(models.Model):
    name = models.TextField(max_length=50)
    image = models.ImageField(null=True)
    
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created']