from rest_framework.viewsets import ModelViewSet
from ..models import Blog
from .serializer import BlogSerializer
class BlogViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
