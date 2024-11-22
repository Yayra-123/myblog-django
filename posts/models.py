from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=55)
    content =models.TextField()
    image =models.ImageField(upload_to='post_image/')
    user =models.ForeignKey(User,on_delete=models.CASCADE)
    
    def _str_init(self):
        return self.title