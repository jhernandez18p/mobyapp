from django.contrib.auth.models import User, Group
from rest_framework import viewsets

from src.api import serializers
from src.blog.models import Post, Comment
from src.base.models import Carousel, CarouselImage
from src.services.models import Service
from src.ventas.models import Photo, Line, SubLine, Color, \
    Type, Provider, Brands, Department, Category, Article


class ServiceViewSet(viewsets.ModelViewSet):
    """ """
    queryset = Service.objects.all()
    serializer_class = serializers.ServiceSerializer


class BrandsViewSet(viewsets.ModelViewSet):
    """ """
    queryset = Brands.objects.all()
    serializer_class = serializers.BrandsSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    """ """
    queryset = Department.objects.all()
    serializer_class = serializers.DepartmentSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """ """
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer


class ArticleViewSet(viewsets.ModelViewSet):
    """ """
    queryset = Article.objects.all()
    serializer_class = serializers.ArticleSerializer


class PhotoViewSet(viewsets.ModelViewSet):
    """ """
    queryset = Photo.objects.all()
    serializer_class = serializers.PhotoSerializer


class LineViewSet(viewsets.ModelViewSet):
    """ """
    queryset = Line.objects.all()
    serializer_class = serializers.LineSerializer


class SubLineViewSet(viewsets.ModelViewSet):
    """ """
    queryset = SubLine.objects.all()
    serializer_class = serializers.SubLineSerializer


class ColorViewSet(viewsets.ModelViewSet):
    """ """
    queryset = Color.objects.all()
    serializer_class = serializers.ColorSerializer


class TypeViewSet(viewsets.ModelViewSet):
    """ """
    queryset = Type.objects.all()
    serializer_class = serializers.TypeSerializer


class ProviderViewSet(viewsets.ModelViewSet):
    """ """
    queryset = Provider.objects.all()
    serializer_class = serializers.ProviderSerializer


class UserViewSet(viewsets.ModelViewSet):
    """ """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = serializers.UserSerializerWithToken


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