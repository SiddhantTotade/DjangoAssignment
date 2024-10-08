from django.urls import path
from .views import TriggerSignalView, TriggerSignalThreadView, AuthorView, BookView,TestView

urlpatterns = [
    path("trigger-signal/", TriggerSignalView.as_view(), name="trigger_signal"),
    path("threading-signal/", TriggerSignalThreadView.as_view(), name="thread_signal"),
    path("authors/", AuthorView.as_view(), name="create_author"),
    path("books/", BookView.as_view(), name="create_book"),
    path("test/", TestView.as_view(), name="test"),
]
