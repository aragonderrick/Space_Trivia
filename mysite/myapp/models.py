from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class suggestionModel(models.Model):
    #pythons object oriented version
    suggestion = models.CharField(max_length=240)
    client = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.suggestion

class CommentModel(models.Model):
    comment = models.CharField(max_length=240)
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    suggestion = models.ForeignKey(suggestionModel, on_delete=models.CASCADE)

    def __str__(self):
        return self.comment

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    points = models.IntegerField(default=0)
    
    def __str__(self):
        return str(self.user)