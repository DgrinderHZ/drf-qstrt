from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Snippet

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """
    User serializer based on PrimaryKey Relationship.
    """
    snippets = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Snippet.objects.all()
    )

    class Meta:
        model = User
        fields = ['id', 'username', 'snippets']


# Variant for fbv.serializers : Using ModelSerializer
class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code',
                  'linenos', 'language', 'style', 'owner']
