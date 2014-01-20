from django.db import models

# Create your models here.
class Photo(models.Model):
    image = models.ImageField(upload_to='photos/')
    upload_date = models.DateTimeField('date uploaded')
    score = models.IntegerField()
    description = models.CharField(max_length=140)
    def __unicode__(self):
        return self.description
