from django.db import models

# Create your models here.
class File(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    # image = models.ImageField(null=True)
    video = models.FileField(null=True, upload_to='videos')
    videolink = models.CharField(max_length=200, blank=True, null=True)


    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created']


class Image(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    height = models.IntegerField(blank=True, default=0, null=True)
    width = models.IntegerField(blank=True, default=0, null=True)
    image = models.ImageField(upload_to='images')
    imagelink = models.CharField(max_length=200, blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)



    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-created']