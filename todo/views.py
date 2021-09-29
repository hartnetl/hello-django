from django.shortcuts import render, redirect
from .models import Item
# Create your views here.


def get_todo_list(request):
    # Let's get a query set of all items in the database
    items = Item.objects.all()
    # context will be a dictionary with all of our items
    context = {
        'items': items
    }
    return render(request, 'todo/todo_list.html', context)


def add_item(request):
    # Our post button is to here, so we need to handle that properly
    if request.method == 'POST':
        # this get the value entered into the input field
        name = request.POST.get('item_name')
        done = 'done' in request.POST

        # Create the new object as per the input fields
        Item.objects.create(name=name, done=done)

        # bring the user back to the updated todo list
        return redirect('get_todo_list')
    return render(request, 'todo/add_item.html')
