from django.test import TestCase
from .models import Image,Category,Location
import datetime as dt
# Create your tests here.

class CategoryTestClass(TestCase):
 # Set up method
    def setUp(self):
        self.travel= Category(name ='travel')

    def test_instance(self):
        self.assertTrue(isinstance(self.travel,Category))
    
    def test_save_method(self):
        self.travel.save_category()
        categorys = Category.objects.all()
        self.assertTrue(len(categorys)> 0)
    
    def test_delete_method(self):
        self.travel.save_category()
        categorys = Category.objects.all()
        self.travel.delete_category()
        categorys = Category.objects.all()
        self.assertTrue(len(categorys)==0)

    

class LocationTestClass(TestCase):
    def setUp(self):
        self.lagos= Location(name ='lagos')

    def test_instance(self):
        self.assertTrue(isinstance(self.lagos,Location))
    
    def test_save_method(self):
        self.lagos.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)> 0)

    def tearDown(self):
        Category.objects.all().delete()
        Location.objects.all().delete()
        Image.objects.all().delete()

    def test_delete_method(self):
        self.lagos.save_location()
        locations = Location.objects.all()
        self.lagos.delete_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)==0)

class ImageTestCase(TestCase):
    def setUp(self):
        """
        This will create a new image before each test case
        """
        self.new_image = Image(name = "dee",description = "i can do it")
    
    def tearDown(self):
        """
        This will clear the db after each test
        """
        Image.objects.all().delete()
        Category.objects.all().delete()
        Location.objects.all().delete()
    
    def test_instance(self):
        """
        This will test whether the new image created is an instance of the Image class
        """
        self.assertTrue(isinstance(self.new_image, Image))

    