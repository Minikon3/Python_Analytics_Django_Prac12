from django.db import models

# Create your models here.
# charts/models.py
from django.db import models

class ChartData(models.Model):
    json_data = models.JSONField()
    chart_image = models.ImageField(upload_to='chart_images/', null=True, blank=True)
