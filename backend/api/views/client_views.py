from rest_framework import viewsets, status
from rest_framework.response import Response
from ..models import Client
from ..serializers import ClientSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        try:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ProtectedError:
            return Response({"detail": "Klienta nelze smazat, protože má přidělený účet."}, status=status.HTTP_400_BAD_REQUEST)