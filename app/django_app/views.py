import logging
import json
import threading
from django.db import transaction
from .models import MyModel, Rectangle
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from django_app.signals import api_trigger_signal
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .signals import my_signal


class TriggerSignalView(APIView):
    def post(self, request, *args, **kwargs):
        logging.info("Before signal trigger.")
        print("Before signal trigger.")

        api_trigger_signal.send(sender=self.__class__)

        logging.info("After signal trigger.")
        print("After signal trigger.")

        return Response({'message': 'Signal triggered successfully!'}, status=200)


@csrf_exempt
def my_view(request):
    print(f"View called in thread: {threading.current_thread().name}")

    my_signal.send(sender=None)

    return HttpResponse("Signal sent!")


@csrf_exempt
def create_my_model(request):
    if request.method == 'POST':
        try:
            if request.content_type == 'application/json':
                data = json.loads(request.body)
                name = data.get("name")
            else:
                name = request.POST.get("name")

            if not name:
                return JsonResponse({'status': 'error', 'message': 'Name field is required.'})

            with transaction.atomic():
                my_model = MyModel(name=name)
                my_model.save()
            return JsonResponse({'status': 'success'})

        except ValueError as e:
            return JsonResponse({'status': 'error', 'message': str(e)})
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON.'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})


def rectangle_view(request):
    rect = Rectangle(length=10, width=5)

    dimensions = [dimension for dimension in rect]

    return JsonResponse(dimensions, safe=False)
