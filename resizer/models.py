from django.db import models

# Create your models here.
class File(models.Model):
    name = models.TextField(max_length=50, null=True)
    # image = models.ImageField(null=True)
    video = models.FileField(null=True)

    
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created']