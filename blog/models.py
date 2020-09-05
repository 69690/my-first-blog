from django.db import models

# Create your models here.
from django.conf import settings
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    # url = models.CharField(max_length=20)
    blog_views = models.IntegerField(default=0)     #,null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class FirstVisit(models.Model): #CHECK IF USER VISITS A STORY FOR THE FIRST TIME
    url = models.URLField()
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

# class PostCount(models.Model):
#     total_views = models.IntegerField(default=0)
#     view_total_count = models.ForeignKey(Post, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.total_views