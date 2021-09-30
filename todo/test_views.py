from django.test import TestCase

# Create your tests here.


class TestDjango(TestCase):

    # here self is the class TestDjango
    def test_this_thing_works(self):
        # test if 1=0
        self.assertEqual(1, 1)
