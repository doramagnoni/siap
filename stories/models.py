from django.db import models
from django.contrib.auth.models import User  
from cloudinary.models import CloudinaryField

class Story(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    
    image = CloudinaryField('image')
    category = models.CharField(max_length=50, blank=True)
    status = models.CharField(max_length=20, choices=(
        ('draft', 'Draft'),
        ('published', 'Published'),
    ), default='draft')

    def __str__(self):
        return self.title
    