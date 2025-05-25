from django.db import models

class NoteModel(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField()
