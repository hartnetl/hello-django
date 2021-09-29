from django.shortcuts import render
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
    return render(request, 'todo/add_item.html')