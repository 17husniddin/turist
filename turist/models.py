from django.db import models

# Create your models here.

class Turist(models.Model):

    name = models.CharField(max_length=300, db_index=True)
    content = models.TextField()
    rasmi = models.CharField(max_length=400)
    # price = models.IntegerField()
    category = models.ForeignKey('Category', on_delete=models.PROTECT)

    class Meta:
        ordering = ['pk']


class Category(models.Model):
    name = models.CharField(max_length=300)

    class Meta:
        ordering = ['name']