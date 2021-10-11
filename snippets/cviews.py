"""
This contains class based views.
"""
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework import permissions, renderers

from qstart.serializers import User
from snippets.permissions import IsOwnerOrReadOnly


from .models import Snippet
from .serializers import SnippetSerializer2, UserSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SnippetList(APIView):
    """
    - List all snippets, or
    - Create a new snippet.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get(self, request, format=None):
        snippets = Snippet.objects.all()
        serialzer = SnippetSerializer2(snippets, many=True)
        return Response(serialzer.data)

    def post(self, request, format=None):
        serializer = SnippetSerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SnippetDetail(APIView):
    """
    - Retrieve,
    - Update,
    - Delete a snippet.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get(self, request, pk, format=None):
        snippet = get_object_or_404(Snippet, pk=pk)
        serializer = SnippetSerializer2(snippet)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = get_object_or_404(Snippet, pk=pk)
        serializer = SnippetSerializer2(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = get_object_or_404(Snippet, pk=pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SnippetHighlight(generics.GenericAPIView):
    queryset = Snippet.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)
# for more shortcuts
# https://www.django-rest-framework.org/tutorial/3-class-based-views/#using-mixins
