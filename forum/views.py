from django.db.models import Count
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import ForumTopic, ForumPost, ForumPostLike
from .serializers import ForumTopicSerializer, ForumPostSerializer


class ForumTopicList(generics.ListCreateAPIView):
    """
    List forum topics or create a topic if logged in.
    """
    serializer_class = ForumTopicSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # Queryset with annotations for post count
    queryset = ForumTopic.objects.annotate(
        posts_count=Count('posts', distinct=True)
    ).order_by('-created_at')

    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]

    filterset_fields = [
        'author__followed__owner__profile', 
        'author__profile',
    ]

    search_fields = [
        'title',
        'author__username',
    ]

    ordering_fields = [
        'created_at',  # Order by creation date (descending by default)
        'posts_count',
    ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ForumTopicDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ForumTopic.objects.all()
    serializer_class = ForumTopicSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ForumPostList(generics.ListCreateAPIView):
    """
    List forum posts or create a post if logged in.
    """
    serializer_class = ForumPostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    queryset = ForumPost.objects.annotate(
        likes_count=Count('likes', distinct=True), 
    ).order_by('-created_at')

    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]

    filterset_fields = [
        'topic',  # Filter by topic
        'author__profile',
        'likes__owner__profile',  
    ]
    
    search_fields = [
        'content',
        'author__username',
    ]
    
    ordering_fields = [
        'created_at',
        'likes_count',
    ]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ForumPostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ForumPost.objects.all()
    serializer_class = ForumPostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
