from django.db import models

# Create your models here.


# we want to inherit the base model class
class Item(models.Model):
    # define the attributes that our individual items will have.
    # charfield means it will be text. null=False and blank=False makes it a
    # required field
    name = models.CharField(max_length=50, null=False, blank=False)
    done = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        return self.name
