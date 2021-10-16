"""
This contains class based views.
"""
from django.http import request
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework import permissions

from .serializers import User
from snippets.permissions import IsOwnerOrReadOnly


from snippets.models import Snippet
from .serializers import SnippetSerializer, UserSerializer


class UserList(generics.ListAPIView):
    """
    generics.ListAPIView based view:
    - List all users.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer(context={'request': request})


class UserDetail(generics.RetrieveAPIView):
    """
    generics.RetrieveAPIView based view:
    - List user details.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer(context={'request': request})


class SnippetList(APIView):
    """
    APIView based view:
    - List all snippets, or
    - Create a new snippet.
    """
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]

    def get(self, request, format=None):
        snippets = Snippet.objects.all()
        serialzer = SnippetSerializer(snippets, many=True, context={'request': request})
        return Response(serialzer.data)

    def post(self, request, format=None):
        serializer = SnippetSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SnippetDetail(APIView):
    """
    APIView based view:
    - Retrieve,
    - Update,
    - Delete a snippet.
    """
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]

    def get(self, request, pk, format=None):
        snippet = get_object_or_404(Snippet, pk=pk)
        serializer = SnippetSerializer(snippet, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        snippet = get_object_or_404(Snippet, pk=pk)
        serializer = SnippetSerializer(snippet, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = get_object_or_404(Snippet, pk=pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
