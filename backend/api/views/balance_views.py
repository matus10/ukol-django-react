from rest_framework import viewsets
from ..models import Balance
from ..serializers import BalanceSerializer

class BalanceViewSet(viewsets.ModelViewSet):
    queryset = Balance.objects.all()
    serializer_class = BalanceSerializer