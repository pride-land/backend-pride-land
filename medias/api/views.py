from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from ..models import Media
from .serializer import MediaSerializer

#test imports
import base64
from io import BytesIO
from PIL import Image as PILImage
from django.core.files.base import ContentFile
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..models import Media
from rest_framework.response import Response
import base64
from django.http import JsonResponse
from django.core.files.base import ContentFile
import json


class MediaViewSet(ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer

@api_view(['GET'])
def uploadImage(request):
    images = Media.objects.all()
    serializer = MediaSerializer(images, many=True)
    return Response(serializer.data)


class MediaViewSet(ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer


@api_view(['GET'])
def imageData(request):
    try:
        dataEntries = Media.objects.all()
        dataList = []

        for elt in dataEntries:
           
            data = int(elt.image_b64, 2).to_bytes((len(elt.image_b64) + 7) // 8, byteorder='big')
            print((elt.image_b64))
            dataList.append({'id': elt.id, 'image_b64': data})
            # print(dataList)
            
            # with open(elt.image_b64, 'rb') as file:
            #         encoded_string = base64.b64decode(file.read())
                    
            # base64_data = base64.b64decode(elt.image_b64)

            # img_data = base64.b64decode(elt.image_b64)
            # print((img_data))

            # img_data = base64.b64decode(elt.image_b64)
            # result = img_data.decode('utf-8')
            
            # print(result)
            # convData = base64.b64encode(img_data).decode('utf-8')
            # print(convData)

        return JsonResponse(dataList, safe=False, status=200)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    
# def __str__(self):
#     return f"URL: {self.image_b64}"