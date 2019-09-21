from django.test import TestCase
from .models import Bucketlist

class ModelTestcase(Testcase):
    def setup(self):
        self.bucketlist_name="Write world class code"
        self.bucketlist=Bucketlist(name=self.bucketlist_name)
    def test_model_can_create_a_bucketlist(self):
        old_count=Bucketlist.objects.count()
        self.bucketlist(save)
        new_count=Bucketlist.object.count()
        self.assertNotEqual(old-count,new_count)
