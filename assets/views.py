from rest_framework.viewsets import ModelViewSet
from .models import Asset
from .serializers import AssetSerializer

class AssetViewSet(ModelViewSet):
    queryset = Asset.objects.all().order_by("-id")
    serializer_class = AssetSerializer
