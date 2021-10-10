from django.contrib.auth.models import Group
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from qstart.serializers import GroupSerializer, User, UserSerializer


class UserViewSet(ModelViewSet):
    """
    API endpoint that allows CRUD on users.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(ModelViewSet):
    """
    API endpoint that alows CRUD on groups.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
