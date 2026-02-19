from django.db import models

# Create your models here.

# About section
class About(models.Model):
    title = models.CharField(max_length=25)
    body = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'About'


# Social Media Links

class Social(models.Model):
    plartform = models.CharField(max_length=25)
    url = models.URLField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.plartform