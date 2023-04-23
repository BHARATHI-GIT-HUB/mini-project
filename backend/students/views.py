from django.shortcuts import render
from django.http.response import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http.response import JsonResponse
from .serializers import StudetSerializer


# Create your views here.

class StudentView(APIView):

    def post(self,request):
        data = request.data
        serializer = StudetSerializer(data= data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse("Sucess",status = 200 ,safe=False)
        else:
            return JsonResponse(serializer.errors,status = 400 ,safe=False)

# {
# "name":"alpha",
# "email":"g@gmail.com"}