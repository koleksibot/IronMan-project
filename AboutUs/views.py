# from django.shortcuts import render
# from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import AboutUsSerializer
from .models import AboutUs


@api_view(['GET'])
def about_us(request):
    try:
        aboutUs = AboutUs.objects.all()
        serializer = AboutUsSerializer(aboutUs, many=True)
        # print(serializer.data)
        return Response(serializer.data)
    except:
        return Response({'Something Went Wrong!'})


