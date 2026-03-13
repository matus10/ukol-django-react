from rest_framework import viewsets, status
from rest_framework.response import Response
from django.db.models.deletion import ProtectedError
from ..models import Client
from ..serializers import ClientSerializer
from ..services.client_service import ClientService

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

    def list (self, request, *args, **kwargs):
        first_name = request.GET.get('first_name')
        last_name = request.GET.get('last_name')
        id_client = request.GET.get('id_client')
        limit = request.GET.get('limit')

        try:
            queryset = ClientService.get_filtered_queryset(first_name=first_name, last_name=last_name, id_client=id_client, limit=limit)
        except ValueError as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        try:
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ProtectedError:
            return Response({"detail": "Klienta nelze smazat, protože má přidělený účet."}, status=status.HTTP_400_BAD_REQUEST)