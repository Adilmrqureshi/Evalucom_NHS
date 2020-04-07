from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

class Bed(models.Model):
    res_beds = models.IntegerField(null=True)
    res_dem_beds = models.IntegerField(null=True)
    nus_beds = models.IntegerField(null=True)
    nus_dem_beds = models.IntegerField(null=True)
    
class Home(models.Model):
    name = models.CharField(max_length=200)
    vacant_beds = models.IntegerField()
    beds = models.ForeignKey(Bed, on_delete=models.CASCADE)
    vacancy_updated = models.DateField(timezone.now())

    def __str__(self):
        return self.name



