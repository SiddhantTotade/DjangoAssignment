import time
import logging
import threading
from django.dispatch import Signal, receiver

# Define custom signals
api_trigger_signal = Signal()
threading_signal = Signal()

# Create a thread-local storage
thread_local = threading.local()

# Signal handler that introduces a 5-second delay


@receiver(api_trigger_signal)
def log_signal_trigger(sender, **kwargs):
    logging.info("Signal handler started.")
    print("Signal handler started.")
    time.sleep(5)  # Simulate a blocking operation with a 5-second delay
    logging.info("Signal handler finished.")
    print("Signal handler finished.")


@receiver(threading_signal)
def modify_thread_local(sender, **kwargs):
    thread_local.value = "Modified in Signal"
