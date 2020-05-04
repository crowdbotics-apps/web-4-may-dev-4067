from rest_framework import authentication
from homefgh.models import Ddfgssfg
from .serializers import DdfgssfgSerializer
from rest_framework import viewsets


class DdfgssfgViewSet(viewsets.ModelViewSet):
    serializer_class = DdfgssfgSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Ddfgssfg.objects.all()
