from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import cviews


snippet_highlight = cviews.SnippetHighlight.as_view()
snippet_list = cviews.SnippetList.as_view()
snippet_detail = cviews.SnippetDetail.as_view()

urlpatterns = [
    path('cbv/snippets/', snippet_list, name='cbv-snippet-list'),
    path('cbv/snippets/<int:pk>/', snippet_detail, name='cbv-snippet-detail'),
    path(
        'cbv/snippets/<int:pk>/highlight/',
        snippet_highlight,
        name='snippet-highlight'
    ),
    path('users/', cviews.UserList.as_view(), name='user-list'),
    path(
        'users/<int:pk>/',
        cviews.UserDetail.as_view(),
        name='user-detail'
    ),
]

urlpatterns = format_suffix_patterns(urlpatterns)
