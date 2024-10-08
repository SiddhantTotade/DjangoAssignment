import time
import logging
import threading
from django.dispatch import Signal, receiver

api_trigger_signal = Signal()
my_signal = Signal()


@receiver(api_trigger_signal)
def log_signal_trigger(sender, **kwargs):
    logging.info("Signal handler started.")
    print("Signal handler started.")
    time.sleep(5)
    logging.info("Signal handler finished.")
    print("Signal handler finished.")


@receiver(my_signal)
def my_signal_handler(sender, **kwargs):
    print(f"Signal handler called in thread: {
          threading.current_thread().name}")
