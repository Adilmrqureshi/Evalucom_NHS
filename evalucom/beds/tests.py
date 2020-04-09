from django.test import TestCase

from . import models

# Create your tests here.
class DeleteAllHomeRecordsTest(TestCase):
    def test_delete_all_records(self):
        """
        If no questions exist, an appropriate message is displayed.
        """
        for i in range(6):
            hello = models.Bed.objects.create(
                res_beds = i,res_dem_beds =i, nus_beds =i, nus_dem_beds =i)
            
        
        hello = models.Bed.objects.all()
        hello.delete()
        self.assertQuerysetEqual(hello, [])
    
    def test_foreign_key(self):
        
        hello = models.Bed.objects.create(
            res_beds = 1,res_dem_beds =1, nus_beds =1, nus_dem_beds =1)
        bye = models.Home.objects.create(
            name = "hello", vacant_beds = 0, beds=hello
        )
        print(bye.pk)
            

