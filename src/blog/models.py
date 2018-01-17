from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE,)
    updated_by = models.ForeignKey(User, null=True, related_name='+', on_delete=models.CASCADE,)
    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=200)
    text = models.TextField()
    background = models.ImageField(blank=True, 
        default='https://static.pexels.com/photos/261579/pexels-photo-261579.jpeg',
        upload_to="post/"
    )
    img = models.ImageField(blank=True, 
        default='/static/base/img/food.jpg',
        upload_to="post/"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title