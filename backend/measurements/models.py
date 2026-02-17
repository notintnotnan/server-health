from django.db import models

class Temperature(models.Model):
    id = models.BigAutoField(primary_key=True)
    interval_end = models.DateTimeField(blank=False, null=False)
    reading = models.DecimalField()

class Frequency(models.Model):
    id = models.BigAutoField(primary_key=True)
    reading_id = models.ForeignKey(
        Temperature,
        on_delete=models.CASCADE,
        related_name='reading'
    )
    frequency = models.DecimalField()
    min_frequency = models.DecimalField()
    max_frequency = models.DecimalField()
