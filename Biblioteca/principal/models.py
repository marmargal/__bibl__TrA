from django.db import models

# Create your models here.
    
class Book(models.Model):
    idBook = models.IntegerField()
    ISBN = models.IntegerField() # max_length ???
    title = models.TextField()
    autor = models.CharField(max_length = 40)
    description = models.TextField()
    stock = models.IntegerField()
    
    def __unicode__(self):
        return self.title


class Reader(models.Model):
    idReader = models.IntegerField()
    name = models.CharField(max_length = 40)
    sex = models.CharField(max_length = 1) # M || F
    book = models.ForeignKey(Book)
    
    def __unicode__(self):
        return self.name
  
    
class Comment(models.Model):
    idComment = models.IntegerField()
    comment = models.TextField()
    stars = models.IntegerField() # [0..5]
    reader = models.ForeignKey(Reader) # esta bien asi??
    book = models.ForeignKey(Book)
    
    def __unicode__(self):
        return self.comment


# bibliotecario
# class     

    