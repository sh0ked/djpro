from django.db import models


class Article(models.Model):
    autor = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    title = models.CharField(max_length=200)
    full_text = models.TextField(max_length=20000)