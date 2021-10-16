from rest_framework import serializers
from django.contrib.auth import get_user_model
from snippets.models import Snippet

User = get_user_model()


# Variant : Using HyperlinkedModelSerializer
class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(
                view_name='hyper-snippet-highlight',
                format='html')

    class Meta:
        model = Snippet
        fields = ['url', 'id', 'highlight', 'owner',
                  'title', 'code', 'linenos', 'language', 'style']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(
                    many=True,
                    view_name='hyper-snippet-detail',
                    read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippets']
