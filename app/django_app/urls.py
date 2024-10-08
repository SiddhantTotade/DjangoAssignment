from django.urls import path
from .views import TriggerSignalView, create_my_model, rectangle_view, my_view

urlpatterns = [
    path("signal-1/", TriggerSignalView.as_view(), name="trigger_signal"),
    path("signal-2/", my_view, name="thread_signal"),
    path('signal-3/', create_my_model, name='create_my_model'),
    path('rectangle/', rectangle_view, name='rectangle_view'),
]
