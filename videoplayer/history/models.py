from django.db import models

class History(models.Model):
    url = models.URLField(max_length = 200)

    # def __str__(self):
    #     return self.url