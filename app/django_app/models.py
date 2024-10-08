from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models

# Create your models here.


class Rectangle(models.Model):
    length = models.IntegerField(null=True, blank=True)
    width = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.length + "  "+self.width)


class Author(models.Model):
    name = models.CharField(max_length=100)
    book_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.id)


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


@receiver(post_save, sender=Book)
def update_author_book_count(sender, instance, created, **kwargs):
    if created:
        # Increment the book count for the author
        author = instance.author
        author.book_count += 1
        author.save()
