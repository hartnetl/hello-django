from django.test import TestCase
from .forms import ItemForm

# Create your tests here.


class TestItemForm(TestCase):

    def test_item_name_is_required(self):
        # We're will test that the form is not valid, the error occurred on
        # the name field and the specific error message is what we expect :

        # instantiate a form without a name to simulate a user not filling
        # in their name
        form = ItemForm({'name': ''})
        # the form shouldn't be valid because no name is entered, so
        # assertFalse is used
        self.assertFalse(form.is_valid())
        # When the form is invalid it should also send back a dictionary of
        # fields on whicht here were errors and the associated error messages
        # This assertIn tells if there's a name key in the dictionary of form
        # errors
        self.assertIn('name', form.errors.keys())
        # assert equal is used to check whether the error message on the name
        # field is "this field is required"
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_done_field_is_not_required(self):
        # Make a form with only a name
        form = ItemForm({'name': 'Test Todo Item'})
        # Test the form is valid
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        # we don't want fields being accidentally displayed, so we need to 
        # make sure the only ones being displayed are written into the
        # metaclass

        # We only need to instantiate an empty form
        form = ItemForm()
        # use assert equal to check meta fields equal to the list given
        self.assertEqual(form.Meta.fields, ['name', 'done'])
