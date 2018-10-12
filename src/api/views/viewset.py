from django.contrib.auth.models import User, Group
from django.contrib.flatpages.models import FlatPage

from django_filters import rest_framework as filters
from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter

from src.api import serializers

from src.base.models import Carousel, CarouselImage, Site, Pages, Position, SocialMedia
from src.blog.models import Post, Comment, Tag
from src.faq.models  import Answer, Question
from src.services.models import Service
from src.testimonials.models import Testimonial
from src.ventas.models import Photo, Line, SubLine, Color, \
    Type, Provider, Brands, Department, Category, Article


class FlatpagesViewSet(viewsets.ModelViewSet):
    """ Questions Viewset """
    # __basic_fields = ('name', 'menu__name', 'menu__description')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = FlatPage.objects.all()
    serializer_class = serializers.FlatpagesSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    # filter_fields = __basic_fields
    # search_fields = __basic_fields


class QuestionsViewSet(viewsets.ModelViewSet):
    """ Questions Viewset """
    # __basic_fields = ('name', 'menu__name', 'menu__description')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Question.objects.all()
    serializer_class = serializers.QuestionsSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    # filter_fields = __basic_fields
    # search_fields = __basic_fields


class AnswersViewSet(viewsets.ModelViewSet):
    """ Answers Viewset """
    # __basic_fields = ('name', 'menu__name', 'menu__description')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Answer.objects.all()
    serializer_class = serializers.AnswersSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    # filter_fields = __basic_fields
    # search_fields = __basic_fields


class TestimonialViewSet(viewsets.ModelViewSet):
    """ Testimonials Viewset """
    # __basic_fields = ('name', 'menu__name', 'menu__description')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Testimonial.objects.all()
    serializer_class = serializers.TestimonialSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    # filter_fields = __basic_fields
    # search_fields = __basic_fields


class PagesViewSet(viewsets.ModelViewSet):
    """ Pages Viewset """
    # __basic_fields = ('name', 'menu__name', 'menu__description')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Pages.objects.all()
    serializer_class = serializers.PagesSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    # filter_fields = __basic_fields
    # search_fields = __basic_fields


class SocialMediaViewSet(viewsets.ModelViewSet):
    """ Social media Viewset """
    # __basic_fields = ('name', 'menu__name', 'menu__description')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = SocialMedia.objects.all()
    serializer_class = serializers.SocialMediaSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    # filter_fields = __basic_fields
    # search_fields = __basic_fields


class PositionViewSet(viewsets.ModelViewSet):
    """ Position Viewset """
    # __basic_fields = ('name', 'menu__name', 'menu__description')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Position.objects.all()
    serializer_class = serializers.PositionSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    # filter_fields = __basic_fields
    # search_fields = __basic_fields


class ServiceViewSet(viewsets.ModelViewSet):
    """ Service Viewset """
    # __basic_fields = ('name', 'menu__name', 'menu__description')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Service.objects.all()
    serializer_class = serializers.ServiceSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    # filter_fields = __basic_fields
    # search_fields = __basic_fields


class SiteViewSet(viewsets.ModelViewSet):
    """ Site Viewset """
    # __basic_fields = ('name', 'menu__name', 'menu__description')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Site.objects.all()
    serializer_class = serializers.SiteSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    # filter_fields = __basic_fields
    # search_fields = __basic_fields


class BrandsViewSet(viewsets.ModelViewSet):
    """ Brand Viewset """
    # __basic_fields = ('name', 'menu__name', 'menu__description')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Brands.objects.all()
    serializer_class = serializers.BrandsSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    # filter_fields = __basic_fields
    # search_fields = __basic_fields


class DepartmentViewSet(viewsets.ModelViewSet):
    """ Departments Viewset """
    # __basic_fields = ('name', 'menu__name', 'menu__description')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Department.objects.all()
    serializer_class = serializers.DepartmentSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    # filter_fields = __basic_fields
    # search_fields = __basic_fields


class CategoryViewSet(viewsets.ModelViewSet):
    """ Category Viewset """
    # __basic_fields = ('name', 'menu__name', 'menu__description')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    # filter_fields = __basic_fields
    # search_fields = __basic_fields


class ArticleViewSet(viewsets.ModelViewSet):
    """ Article Viewset """
    __basic_fields = ('code','description')
    __filter_fields = ('line','category','department','brand','color')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Article.objects.all().order_by('-featured')
    serializer_class = serializers.ArticleSerializer
    lookup_field = 'slug'
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = __filter_fields
    search_fields = __basic_fields


class PhotoViewSet(viewsets.ModelViewSet):
    """ Photo Viewset """
    # __basic_fields = ('name', 'menu__name', 'menu__description')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Photo.objects.all()
    serializer_class = serializers.PhotoSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    # filter_fields = __basic_fields
    # search_fields = __basic_fields


class LineViewSet(viewsets.ModelViewSet):
    """ Line Viewset """
    __filter_fields = ('description', 'name', 'code', 'count')
    __basic_fields = ('description', 'name', 'code')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Line.objects.all()
    serializer_class = serializers.LineSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = __filter_fields
    search_fields = __basic_fields


class SubLineViewSet(viewsets.ModelViewSet):
    """ Subline Viewset """
    __filter_fields = ('parent')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = SubLine.objects.all()
    serializer_class = serializers.SubLineSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = __basic_fields
    # search_fields = __basic_fields


class ColorViewSet(viewsets.ModelViewSet):
    """ Color Viewset """
    # __basic_fields = ('name', 'menu__name', 'menu__description')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Color.objects.all()
    serializer_class = serializers.ColorSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    # filter_fields = __basic_fields
    # search_fields = __basic_fields


class TypeViewSet(viewsets.ModelViewSet):
    """ Type Viewset """
    # __basic_fields = ('name', 'menu__name', 'menu__description')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Type.objects.all()
    serializer_class = serializers.TypeSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    # filter_fields = __basic_fields
    # search_fields = __basic_fields


class ProviderViewSet(viewsets.ModelViewSet):
    """ Provider Viewset """
    # __basic_fields = ('name', 'menu__name', 'menu__description')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Provider.objects.all()
    serializer_class = serializers.ProviderSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    # filter_fields = __basic_fields
    # search_fields = __basic_fields


class UserViewSet(viewsets.ModelViewSet):
    """ User Viewset """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = serializers.UserSerializerWithToken
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    # filter_fields = __basic_fields
    # search_fields = __basic_fields


class GroupViewSet(viewsets.ModelViewSet):
    """ Group Viewset """
    # __basic_fields = ('name', 'menu__name', 'menu__description')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    # filter_fields = __basic_fields
    # search_fields = __basic_fields


class PublicBlogPostViewSet(viewsets.ModelViewSet):
    """ Blog Posts Viewset """
    # __basic_fields = ('name', 'menu__name', 'menu__description')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all().filter(is_public=True)
    serializer_class = serializers.BlogPostSerializer
    lookup_field = 'slug'
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    # filter_fields = __basic_fields
    # search_fields = __basic_fields


class BlogPostCommetViewSet(viewsets.ModelViewSet):
    """ Blog Post Commnents Viewset """
    __basic_fields = ('id', 'content', 'approved','timestamp','object_id','author','parent','post','content_type')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = serializers.BlogPostCommentsSerializer
    # lookup_field = 'slug'
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    filter_fields = __basic_fields
    search_fields = __basic_fields


class BlogTagViewSet(viewsets.ModelViewSet):
    """ Blog Post Commnents Viewset """
    # __basic_fields = ('name', 'menu__name', 'menu__description')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Tag.objects.all()
    serializer_class = serializers.BlogTagSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)


class FrontendCarouselViewSet(viewsets.ModelViewSet):
    """ Frontend Carrousel Viewet """
    # __basic_fields = ('name', 'menu__name', 'menu__description')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Carousel.objects.all()
    serializer_class = serializers.FrontendCarouselSerializer
    # filter_fields = __basic_fields
    # search_fields = __basic_fields


class FrontendCarouselImageViewSet(viewsets.ModelViewSet):
    """ Frontend Carrousel Images Viewet """
    # __basic_fields = ('name', 'menu__name', 'menu__description')
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = CarouselImage.objects.all()
    serializer_class = serializers.FrontendCarouselImageSerializer
    # filter_fields = __basic_fields
    # search_fields = __basic_fields