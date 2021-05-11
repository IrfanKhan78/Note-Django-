from django.db import models

# Create your models here.

class Note(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(blank=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Note {}'.format(self.id)

    class Meta:
        verbose_name_plural = 'Notes'
