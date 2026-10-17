from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Faculty, Direction, Group
from .serializers import FacultySerializer, DirectionSerializer, GroupSerializer


class FacultyViewSet(viewsets.ModelViewSet):
    queryset = Faculty.objects.all()
    serializer_class = FacultySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class DirectionViewSet(viewsets.ModelViewSet):
    queryset = Direction.objects.select_related('faculty').all()
    serializer_class = DirectionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_fields = ['faculty']


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.select_related('direction', 'direction__faculty').all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_fields = ['direction']