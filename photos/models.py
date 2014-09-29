from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Photo(models.Model):
    image = models.ImageField()
    upload_date = models.DateTimeField('date uploaded')
    rating = models.IntegerField()
    description = models.CharField(max_length=140)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.description
