from django.urls import path
from .views import StoryList, StoryDetail

urlpatterns = [
    path('api/stories/', StoryList.as_view(), name='story-list'),
    path('api/stories/<int:pk>/', StoryDetail.as_view(), name='story-detail'),
]