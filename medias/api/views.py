from rest_framework.viewsets import ModelViewSet
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

class MediaViewSet(ModelViewSet):
    queryset = Media.objects.all()
    serializer_class = MediaSerializer

@api_view(['POST'])
def upload_image(request):
    image_data = request.data.get('image')
    
    if image_data:
        # Decode the Base64 image data
        format, imgstr = image_data.split(';base64,')
        ext = format.split('/')[-1]
        img = PILImage.open(BytesIO(base64.b64decode(imgstr)))

        # Save the image to a file
        img_io = BytesIO()
        img.save(img_io, format=ext)
        img_file = ContentFile(img_io.getvalue(), f'image.{ext}')

        # Save to the database
        image = Media(image=img_file)
        image.save()
        
        return Response({'status': 'Image uploaded successfully'}, status=status.HTTP_201_CREATED)
    return Response({'error': 'No image data provided'}, status=status.HTTP_400_BAD_REQUEST)
