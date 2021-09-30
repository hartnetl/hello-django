from django.test import TestCase
from .models import Item

# Create your tests here.


class TestViews(TestCase):

    # test we can get the home page / todo list html
    def test_get_todo_list(self):
        # slash is the home page url
        response = self.client.get('/')
        # We can then use assert equal to confirm that the response.status
        # code is equal to 200
        self.assertEqual(response.status_code, 200)
        # To confirm the view uses the correct template use
        # self.assertTemplateUsed and tell it the template we expect it to
        # use in the response.
        self.assertTemplateUsed(response, 'todo/todo_list.html')

    # test we can get the add item page
    def test_get_add_item(self):
        # Copy the above test and change the URLs and template used
        response = self.client.get('/add')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/add_item.html')

    # test we can get the edit item page
    def test_get_edit_item(self):
        # create a test item
        item = Item.objects.create(name='Test Todo Item')
        # give the item to edit an id
        response = self.client.get(f'/edit/{item.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/edit_item.html')

    # test we can add an item
    def test_can_add_item(self):
        # make sure items get added
        response = self.client.post('/add', {'name': 'Test Added Item'})
        # make sure you get redirected to the home page after item is added
        self.assertRedirects(response, '/')

    # test we can toggle an item
    def test_can_toggle_item(self):
        # set value to True
        item = Item.objects.create(name='Test Todo Item', done=True)
        response = self.client.get(f'/toggle/{item.id}')
        self.assertRedirects(response, '/')
        # Find the toggled item
        updated_item = Item.objects.get(id=item.id)
        # confirm its now false
        self.assertFalse(updated_item.done)

    # test we can delete an item
    def test_can_delete_item(self):
        item = Item.objects.create(name='Test Todo Item')
        response = self.client.get(f'/delete/{item.id}')
        self.assertRedirects(response, '/')
        # Check if you can find the item you just deleted
        existing_items = Item.objects.filter(id=item.id)
        # Check that the variable you just created is empty
        self.assertEqual(len(existing_items), 0)

    def test_can_edit_item(self):
        item = Item.objects.create(name='Test Todo Item')
        response = self.client.post(f'/edit/{item.id}',
                                    {'name': 'Updated Name'})
        self.assertRedirects(response, '/')
        updated_item = Item.objects.get(id=item.id)
        self.assertEqual(updated_item.name, 'Updated Name')
