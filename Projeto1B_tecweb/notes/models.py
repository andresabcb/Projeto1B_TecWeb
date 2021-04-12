from django.db import models

class Note(models.Model):
    # models.Model - herdando dessa classe
    # __init__() automático
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=500)
    #tag = models.CharField(max_length=150, default="")
    tag = models.CharField(max_length=150)

    def __str__(self):
        id = self.id
        title = self.title
        string = ("'{0}'.'{1}'".format(id,title))
        return string