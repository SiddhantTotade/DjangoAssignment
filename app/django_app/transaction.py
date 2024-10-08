from django.db import transaction
from django.core.exceptions import ObjectDoesNotExist
from .models import Author, Book  # Adjust the import based on your app structure


def create_book_with_transaction(author_name):
    # Create an Author first
    author = Author.objects.create(name=author_name)

    try:
        with transaction.atomic():
            # Create a new Book instance
            book = Book.objects.create(title="New Book", author=author)
            print(f"Created Book: {book.title}")

            # Uncomment the next line to simulate an error
            # raise Exception("Simulated error to force rollback")

    except Exception as e:
        print(f"Error occurred: {e}. The transaction will be rolled back.")

    # Check the author's book count
    try:
        author.refresh_from_db()
        print(f"Author: {author.name}, Book Count: {author.book_count}")
    except ObjectDoesNotExist:
        print("Author does not exist.")


# Run the test
create_book_with_transaction("John Doe")
