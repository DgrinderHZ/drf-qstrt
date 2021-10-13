"""
This contains func. based views.
"""
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.renderers import StaticHTMLRenderer
from rest_framework.response import Response
from rest_framework.reverse import reverse
from snippets.models import Snippet
from snippets.permissions import IsOwnerOrReadOnly
from .serializers import SnippetSerializer
from django.shortcuts import get_object_or_404


@api_view(['GET'])
def api_root(request, format=None):
    """
    Function based view:
    -  Snippets API root.
    """
    return Response({
        'users': reverse('cbv-user-list', request=request, format=format),
        'fbv_snippets': reverse('snippet-list', request=request, format=format),
        'snippets': reverse('cbv-snippet-list', request=request, format=format)
    })


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly])
def snippet_list(request, format=None):
    """
    Function based view:
    - List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        # Get instances
        snippets = Snippet.objects.all()
        # Serialize them
        serializer = SnippetSerializer(snippets, many=True)
        # Return
        return Response(serializer.data)

    elif request.method == 'POST':
        # Serialize
        serializer = SnippetSerializer(data=request.data)
        # Create
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly])
def snippet_detail(request, pk, format=None):
    """
    Function based view:
    - Retrieve,
    - Update or
    - Delete a code snippet.
    """
    snippet = get_object_or_404(Snippet, pk=pk)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SnippetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@renderer_classes([StaticHTMLRenderer])
@permission_classes([IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly])
def snippet_highlight(request, pk, format=None):
    snippet = get_object_or_404(Snippet, pk=pk)
    html = snippet.highlighted
    return Response(html)
