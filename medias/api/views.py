import base64
from ..models import Media
from ..models import Media
from rest_framework import status
from django.http import JsonResponse
from .serializer import MediaSerializer
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import api_view

class MediaViewSet(ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer

@api_view(['POST'])
def uploadImage(request):
    print("WILLLLLL")
    if request.method == "POST":
        # Access the JSON data
        img_base64 = request.data.get("blob_img")
        if img_base64:
            decodedImg = base64.decodebytes(img_base64.encode('utf-8'))
            blobImg = Media(blob_img=decodedImg)
            blobImg.save()
            return JsonResponse({"message": "Image saved successfully"}, status=status.HTTP_201_CREATED)
        return JsonResponse({"error": "No image provided"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def imageData(request):
    try:
        dataEntries = Media.objects.all()
        dataList = []

        for elt in dataEntries:
            
            baseBinary = base64.b64encode(elt.blob_img).decode('utf-8')
            dataList.append({ 'id' : elt.id, 
                             'set_as_hero': elt.set_as_hero,
                             'alt_text' : elt.alt_text,
                             'blob_img' : baseBinary
                             })

        return JsonResponse(dataList, safe=False, status=200)

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

@api_view(['DELETE'])
def deleteImage(request, pk):
    user = Media.objects.get(id=pk)
    user.delete()
    
    return Response('Item successfully deleted!')