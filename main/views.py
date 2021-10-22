from django.db.models.query import QuerySet
from rest_framework.generics import RetrieveAPIView
from .models import Profile
from .serializers import ProfileSerialzer


class ProfileApiView(RetrieveAPIView):
    model = Profile
    serializer_class = ProfileSerialzer
    queryset = Profile.objects.all()
