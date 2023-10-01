from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response
# Create your views here.

from .serializers import TimestampSerializer

class TimestampView(views.APIView):
    def get(self, request, date=None):
        # Process the date and return JSON response
        # Use TimestampSerializer to serialize the data
        # Return Response(TimestampSerializer(data).data)
        pass