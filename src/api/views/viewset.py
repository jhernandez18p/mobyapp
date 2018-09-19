from django.contrib.auth.models import User, Group
from django.contrib.flatpages.models import FlatPage

from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response

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
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = FlatPage.objects.all()
    serializer_class = serializers.FlatpagesSerializer


class QuestionsViewSet(viewsets.ModelViewSet):
    """ Questions Viewset """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Question.objects.all()
    serializer_class = serializers.QuestionsSerializer


class AnswersViewSet(viewsets.ModelViewSet):
    """ Answers Viewset """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Answer.objects.all()
    serializer_class = serializers.AnswersSerializer


class TestimonialViewSet(viewsets.ModelViewSet):
    """ Testimonials Viewset """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Testimonial.objects.all()
    serializer_class = serializers.TestimonialSerializer


class PagesViewSet(viewsets.ModelViewSet):
    """ Pages Viewset """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Pages.objects.all()
    serializer_class = serializers.PagesSerializer


class SocialMediaViewSet(viewsets.ModelViewSet):
    """ Social media Viewset """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = SocialMedia.objects.all()
    serializer_class = serializers.SocialMediaSerializer


class PositionViewSet(viewsets.ModelViewSet):
    """ Position Viewset """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Position.objects.all()
    serializer_class = serializers.PositionSerializer


class ServiceViewSet(viewsets.ModelViewSet):
    """ Service Viewset """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Service.objects.all()
    serializer_class = serializers.ServiceSerializer


class SiteViewSet(viewsets.ModelViewSet):
    """ Site Viewset """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Site.objects.all()
    serializer_class = serializers.SiteSerializer


class BrandsViewSet(viewsets.ModelViewSet):
    """ Brand Viewset """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Brands.objects.all()
    serializer_class = serializers.BrandsSerializer


class DepartmentViewSet(viewsets.ModelViewSet):
    """ Departments Viewset """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Department.objects.all()
    serializer_class = serializers.DepartmentSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """ Category Viewset """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer


class ArticleViewSet(viewsets.ModelViewSet):
    """ Article Viewset """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Article.objects.all().order_by('-featured')
    serializer_class = serializers.ArticleSerializer


class PhotoViewSet(viewsets.ModelViewSet):
    """ Photo Viewset """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Photo.objects.all()
    serializer_class = serializers.PhotoSerializer


class LineViewSet(viewsets.ModelViewSet):
    """ Line Viewset """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Line.objects.all()
    serializer_class = serializers.LineSerializer


class SubLineViewSet(viewsets.ModelViewSet):
    """ Subline Viewset """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = SubLine.objects.all()
    serializer_class = serializers.SubLineSerializer


class ColorViewSet(viewsets.ModelViewSet):
    """ Color Viewset """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Color.objects.all()
    serializer_class = serializers.ColorSerializer


class TypeViewSet(viewsets.ModelViewSet):
    """ Type Viewset """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Type.objects.all()
    serializer_class = serializers.TypeSerializer


class ProviderViewSet(viewsets.ModelViewSet):
    """ Provider Viewset """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Provider.objects.all()
    serializer_class = serializers.ProviderSerializer


class UserViewSet(viewsets.ModelViewSet):
    """ User Viewset """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = serializers.UserSerializerWithToken


class GroupViewSet(viewsets.ModelViewSet):
    """ Group Viewset """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Group.objects.all()
    serializer_class = serializers.GroupSerializer


class PublicBlogPostViewSet(viewsets.ModelViewSet):
    """ Blog Posts Viewset """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all().filter(is_public=True)
    serializer_class = serializers.BlogPostSerializer


class BlogPostCommetViewSet(viewsets.ModelViewSet):
    """ Blog Post Commnents Viewset """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    serializer_class = serializers.BlogPostCommentsSerializer


class BlogTagViewSet(viewsets.ModelViewSet):
    """ Blog Post Commnents Viewset """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Tag.objects.all()
    serializer_class = serializers.BlogTagSerializer


class FrontendCarouselViewSet(viewsets.ModelViewSet):
    """ Frontend Carrousel Viewet """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Carousel.objects.all()
    serializer_class = serializers.FrontendCarouselSerializer


class FrontendCarouselImageViewSet(viewsets.ModelViewSet):
    """ Frontend Carrousel Images Viewet """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = CarouselImage.objects.all()
    serializer_class = serializers.FrontendCarouselImageSerializer