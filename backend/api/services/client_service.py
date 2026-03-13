from ..models import Client

class ClientService:
    @staticmethod
    def get_filtered_queryset(first_name=None, last_name=None, id_client=None, limit=None):
        queryset = Client.objects.all()

        if first_name:
            queryset = queryset.filter(first_name__icontains=first_name)

        if last_name:
            queryset = queryset.filter(last_name__icontains=last_name)
        
        if id_client:
            try:
                id_client = int(id_client)
                queryset = queryset.filter(id_client=id_client)
            except ValueError:
                raise ValueError("ID klienta musí být číslo.")

        if limit:
            try:
                limit=int(limit)
                queryset = queryset[:limit]
            except ValueError:
                raise ValueError("Limit musí být číslo.")

        return queryset