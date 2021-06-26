from django.db import models


class Sentence(models.Model):
    author = models.CharField(max_length=255, db_index=True)
    book = models.CharField(max_length=255)
    sentence = models.CharField(max_length=2048)
