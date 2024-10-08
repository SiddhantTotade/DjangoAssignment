import logging
from rest_framework.response import Response
from rest_framework.views import APIView
from django_app.signals import api_trigger_signal, threading_signal, thread_local
from .serializers import BookSerializer, AuthorSerializer
from rest_framework import status


class TriggerSignalView(APIView):
    def post(self, request, *args, **kwargs):
        logging.info("Before signal trigger.")
        print("Before signal trigger.")  # Debug print

        api_trigger_signal.send(sender=self.__class__)

        logging.info("After signal trigger.")
        print("After signal trigger.")  # Debug print

        return Response({'message': 'Signal triggered successfully!'}, status=200)


class TriggerSignalThreadView(APIView):
    def post(self, request, *args, **kwargs):
        logging.info("Before signal trigger.")
        print("Before signal trigger.")  # Debug print

        # Check the initial value of the thread-local variable
        initial_value = getattr(thread_local, 'value', 'Not modified')
        logging.info(f"Initial thread-local value: {initial_value}")
        print(f"Initial thread-local value: {initial_value}")  # Debug print

        # Trigger the signal
        threading_signal.send(sender=self.__class__)

        # Check the value after triggering the signal
        final_value = getattr(thread_local, 'value', 'Not modified')
        logging.info(f"Final thread-local value: {final_value}")
        print(f"Final thread-local value: {final_value}")  # Debug print

        return Response({'message': 'Signal triggered successfully!'}, status=200)


class AuthorView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            author = serializer.save()
            return Response(AuthorSerializer(author).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            book = serializer.save()
            return Response(BookSerializer(book).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TestView(APIView):
    def post(self, request):
        print(request.data)
        return Response({"msg": "Hello"}, status=status.HTTP_200_OK)
