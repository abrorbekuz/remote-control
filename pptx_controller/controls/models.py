from django.db import models

class COMMAND(models.Model):
    link = models.CharField(max_length=400)
    k_command = models.CharField(max_length=400)
    description = models.TextField()

    def __str__(self):
        return f'{self.link} | {self.description[:50]}'

