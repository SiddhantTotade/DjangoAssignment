from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models

# Create your models here.


class MyModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)


class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        # This method allows the Rectangle instance to be iterable.
        yield {'length': self.length}
        yield {'width': self.width}


@receiver(post_save, sender=MyModel)
def my_model_post_save(sender, instance, created, **kwargs):
    if created:
        print(f"{instance.name} has been created.")
