from rest_framework.viewsets import ModelViewSet
from ..models import Feedback
from .serializer import FeedbackSerializer

class FeedbackViewSet(ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer