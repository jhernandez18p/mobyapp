from django.contrib.auth import authenticate
from django.contrib.auth.models import User, Group
from django.contrib.flatpages.models import FlatPage

from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework_jwt.settings import api_settings
from rest_framework.validators import UniqueValidator


from src.faq.models import Answer, Question
from src.blog.models import Post, Comment, Tag
from src.base.models import Carousel, CarouselImage, Site, Pages, Position, SocialMedia
from src.user.models import Profile
from src.services.models import Service, ServiceImage
from src.testimonials.models import Testimonial
from src.ventas.models import Line, SubLine, Color, \
    Type, Provider, Brands, Department, Category, Article


"""
Flatpages Serializers
"""


class FlatpagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = FlatPage
        fields = '__all__'


"""
Frecuente Asked Questions Serializers
"""


class QuestionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = '__all__'


class AnswersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = '__all__'


"""
User & auth Serializers
"""


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'
        # fields = ('url', 'name')


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        Token.objects.create(user=user)
        return user

    # class Meta:
    #     model = User
    #     exclude = ('groups', 'user_permissions')
    #     fields = ('id', 'username', 'email', 'password')
    #     fields = '__all__'


class UserSerializerWithToken(serializers.ModelSerializer):

    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True, required=False)

    def get_token(self, obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)
        return token

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    class Meta:
        model = User
        # fields = '__all__'
        # fields = (
        #     'token', 'username', 'first_name', 'last_name', 'email', 'groups', 'is_superuser', 'is_active', 'password'
        # )
        exclude = ('groups', 'user_permissions')


class CreateUserSerializer(serializers.ModelSerializer):

    username = serializers.CharField()
    password = serializers.CharField()
    email = serializers.CharField()

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'], validated_data['password'], validated_data['email'])
        return user


class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError(
            "Unable to log in with provided credentials.")


"""
Blog  Serializers
"""


class BlogPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class BlogPostCommentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'


class BlogTagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'


"""
Services Serializers
"""


class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = '__all__'


class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServiceImage
        fields = '__all__'
        

"""
Testimonial Serializers
"""


class TestimonialSerializer(serializers.ModelSerializer):

    class Meta:
        model = Testimonial
        fields = '__all__'


"""
Site Serializers
"""


class FrontendCarouselSerializer(serializers.ModelSerializer):

    # page = serializers.PrimaryKeyRelatedField( read_only=True )
    # position = serializers.PrimaryKeyRelatedField( read_only=True )
    # images = serializers.PrimaryKeyRelatedField(many=True,)

    class Meta:
        model = Carousel
        fields = '__all__'


class FrontendCarouselImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarouselImage
        fields = '__all__'


class PagesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pages
        fields = '__all__'


class PositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Position
        fields = '__all__'


class SiteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Site
        fields = '__all__'


class SocialMediaSerializer(serializers.ModelSerializer):

    class Meta:
        model = SocialMedia
        fields = '__all__'


"""
Ventas Serializers
"""


class SubLineSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubLine
        fields = '__all__'


class ColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Color
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = '__all__'


class BrandsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brands
        fields = '__all__'


class LineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Line
        fields = '__all__'


class ProviderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Provider
        fields = '__all__'
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class TypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Type
        fields = '__all__'
