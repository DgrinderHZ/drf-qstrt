from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from snippets.cviews import SnippetHighlight


snippet_highlight = SnippetHighlight.as_view()
snippet_list = views.SnippetList.as_view()
snippet_detail = views.SnippetDetail.as_view()

urlpatterns = [
    path('hyper/snippets/', snippet_list, name='hyper-snippet-list'),
    path('hyper/snippets/<int:pk>/', snippet_detail, name='hyper-snippet-detail'),
    path(
        'hyper/snippets/<int:pk>/highlight/',
        snippet_highlight,
        name='hyper-snippet-highlight'
    ),
    path('hyper/users/', views.UserList.as_view(), name='hyper-user-list'),
    path(
        'hyper/users/<int:pk>/',
        views.UserDetail.as_view(),
        name='hyper-user-detail'
    ),
]

urlpatterns = format_suffix_patterns(urlpatterns)
