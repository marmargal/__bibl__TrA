from django.db import models

# Create your models here.

class Book(models.Model):
    
    category = models.TextField()
    title = models.TextField()
    autor = models.CharField(max_length = 40)

    
    def __unicode__(self):
        return self.title