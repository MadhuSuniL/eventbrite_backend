from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.generics import ListAPIView, CreateAPIView, GenericAPIView
from .models import Event
from .serializers import EventSerialzer


class AllEventsView(ListAPIView):
    serializer_class = EventSerialzer
    queryset = Event.objects.all().order_by('date').order_by('time')
    authentication_classes = []
    permission_classes = []


class CreateEventView(CreateAPIView):
    serializer_class = EventSerialzer
    queryset = Event.objects.all()
    # authentication_classes = []
    # permission_classes = []


class UserEvents(GenericAPIView):
    serializer_class = EventSerialzer
    queryset = Event.objects.all()
    # authentication_classes = []
    # permission_classes = []
    
    def get(self,request):
        print(request.user)
        id = request.user.id
        # id = 1
        user = User.objects.get(id=id)
        events = Event.objects.filter(user=user).order_by('date').order_by('time')
        data = self.serializer_class(events,many=True).data

        return Response(data,200)
    
    