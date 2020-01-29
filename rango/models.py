from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True) #< every name is unique. can be used as pk
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    
    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):#< equivilant of toString() in java
        return self.name


class Page(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)#< fk one to many relationships
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title
