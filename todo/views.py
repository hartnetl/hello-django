from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm

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
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('get_todo_list')

    form = ItemForm()
    context = {
        'form': form
    }
    return render(request, 'todo/add_item.html', context)


def edit_item(request, item_id):
    # Get a copy of the item from the database using a django shortcut
    # This searches the database for the clicked item, or returns a 404 
    # error if it doesn't exist
    item = get_object_or_404(Item, id=item_id)

    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
        return redirect('get_todo_list')

    # instance=item prepoulates the form with the information we just got 
    # from the database and stored in the variable item
    form = ItemForm(instance=item)
    context = {
        'form': form
    }

    return render(request, 'todo/edit_item.html', context)
