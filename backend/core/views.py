from rest_framework import viewsets
from .models import CompanyInfo
from .serializers import CompanyInfoSerializer

class CompanyInfoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows company information to be viewed or edited.
    """
    queryset = CompanyInfo.objects.all()
    serializer_class = CompanyInfoSerializer
