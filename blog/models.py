from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    # Title field with max length 100
    title = models.CharField(max_length=100)
    # Content field
    content = models.TextField()
    # Date object with default=current datetime
    date_posted = models.DateTimeField(default=timezone.now)
    # Auther foreign key with cascade ie delete all posts when author deleted
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
