from django.db import models

from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    img_url = models.URLField(default="https://tinyurl.com/ya7cncz6")

    def __str__(self):
        return f"{self.user.username} : {self.img_url}"
    