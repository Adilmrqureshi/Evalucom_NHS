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
        """
            test if the model's fields are working correctly
        """
        hello = models.Bed.objects.create(
            res_beds = 1,res_dem_beds =1, nus_beds =1, nus_dem_beds =1)
        bye = models.Home.objects.create(
            name = "hello", vacant_beds = 0, beds=hello
        )
        bye.id = 0
        print(bye.id)
    
    def test_save_changes_to_models(self):
        """
            Check to see if the changes made to a 
        """
        bed = models.Bed.objects.create(
                res_beds = 2, res_dem_beds = 1,nus_beds = 1, nus_dem_beds = 1 )
        home = models.Home.objects.create(
            
            name = "home_name", vacant_beds = 1, beds = bed, page_number = 1
        )
        home.beds.res_beds -= 1
        home.save()
        print(home.beds.res_beds)
            

