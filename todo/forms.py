from django import forms
from .models import Item

# Our form will be a class that inherits a built-in Django class to give it
# some basic functionality.


# Set up form by giving it a main class which inherits the functionality of
# ModelForm
class ItemForm(forms.ModelForm):
    # This inner class tells the form about itself - which fields it should
    # render, how it should display error messages etc.
    # If you change this our test in test_forms.py will fail
    class Meta:
        model = Item
        fields = ['name', 'done']
