from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify


class Post(models.Model):
    title=models.CharField(max_length=99)
    slug = models.SlugField(unique=True, null=False)
    topic= models.CharField(max_length=50,default='Select')
    images=models.ImageField(upload_to='images',blank=True)
    content= models.TextField()
    # content =HTMLField()
    date_posted=models.DateTimeField(default=timezone.now)
    author=models.ForeignKey(User,default="Anonymous user",on_delete=models.CASCADE)



    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail',kwargs={'pk':self.pk})






