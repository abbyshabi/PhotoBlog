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

    def test_update_method(self):
        editor = Editor.filter_editor('James')
        fetch_editor = Editor.objects.get(first_name='Nick')
        self.assertEqual(fetch_editor.first_name,'Nick')
    

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
    def setup(self):
        self.