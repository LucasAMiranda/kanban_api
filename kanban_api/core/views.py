from rest_framework import viewsets
from .models import Cards   
from .serializers import CardSerializer



class CardViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Cards.objects.all()
    serializer_class = CardSerializer
    


