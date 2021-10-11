from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views, cviews


urlpatterns = [
    path('snippets/', views.snippet_list, name='snippet-list'),
    path('snippets/<int:pk>/', views.snippet_detail),
    path('cbv/snippets/', cviews.SnippetList.as_view()),
    path('cbv/snippets/<int:pk>/', cviews.SnippetDetail.as_view()),
    path('u/', cviews.UserList.as_view(), name='user-list'),
    path('u/<int:pk>/', cviews.UserDetail.as_view()),
    path('sroot/', views.api_root),
    path('snippets/<int:pk>/highlight/', cviews.SnippetHighlight.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
