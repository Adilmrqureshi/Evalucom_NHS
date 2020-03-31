from django.db import models

# Create your models here.

class Bed(models.Model):
    beds = models.IntegerField(default=0)
    dementia_beds = models.IntegerField(default=0)

class Address(models.Model):
    line_1 = models.CharField(max_length=100)
    line_2 = models.CharField(max_length=100)
    line_3 = models.CharField(max_length=100)
    post_code = models.CharField(max_length=8)
    
class Home(models.Model):
    name = models.CharField(max_length=200)
    provider = models.CharField(max_length=200)
    local_authority = models.CharField(max_length=20)
    full_address = models.ForeignKey(Address, on_delete=models.CASCADE)
    no_beds = models.IntegerField(default=0)
    vacant_beds = models.IntegerField()
    closed = models.BooleanField(default=False)
    beds = models.ForeignKey(Bed, on_delete=models.CASCADE)
    vacancy_updated = models.DateField('last updated')

