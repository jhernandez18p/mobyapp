from django.contrib.auth.models import User, Group
from rest_framework import viewsets

from src.blog.models import Post, Comment
from src.base.models import Carousel, CarouselImage
from app.serializers import serializers


class UserViewSet(viewsets.ModelViewSet):
    """ """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = serializers.UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """ """
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer


class BlogPostViewSet(viewsets.ModelViewSet):
    """ """
    queryset = Post.objects.all()
    serializer_class = serializers.BlogPostSerializer


class BlogPostCommetViewSet(viewsets.ModelViewSet):
    """ """
    queryset = Comment.objects.all()
    serializer_class = serializers.BlogPostCommentsSerializer


class FrontendCarouselViewSet(viewsets.ModelViewSet):
    """ """
    queryset = Carousel.objects.all()
    serializer_class = serializers.FrontendCarouselSerializer


class FrontendCarouselImageViewSet(viewsets.ModelViewSet):
    """ """
    queryset = CarouselImage.objects.all()
    serializer_class = serializers.FrontendCarouselImageSerializer