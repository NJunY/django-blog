from django.db import models
from user.models import User

# Create your models here.
class Blog(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=50, default=None, verbose_name='blog code')
    title = models.CharField(max_length=255, default=None, verbose_name='blog title')
    body = models.TextField( default=None, verbose_name='blog content')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_blog')

    time_created = models.DateTimeField(auto_now_add=True, verbose_name='created time')
    time_updated = models.DateTimeField(auto_now=True, verbose_name='updated time')

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = 'Blogs'
    
    def __str__(self):
        return self.code