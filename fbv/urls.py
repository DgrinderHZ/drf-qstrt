from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns


from . import views


urlpatterns = [
    path('fbv/snippets/', views.snippet_list, name='snippet-list'),
    path('fbv/snippets/<int:pk>/', views.snippet_detail, name='snippet-detail'),
    path(
        'fbv/snippets/<int:pk>/highlight/',
        views.snippet_highlight,
        name='snippet-highlight'
    ),
    path('', views.api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)
