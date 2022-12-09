from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, verbose_name='user name')
    code = models.CharField(max_length=50, verbose_name='user code')

    is_active = models.BooleanField(default=True, verbose_name='user is active')

    time_created = models.DateTimeField(auto_now_add=True, verbose_name='created time')
    time_updated = models.DateTimeField(auto_now=True, verbose_name='updated time')

    class Meta:
        ordering = ['-time_updated']
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.code

