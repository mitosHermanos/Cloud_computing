from django.db import models

class Counter(models.Model):
    count_num = models.PositiveIntegerField(default=0)