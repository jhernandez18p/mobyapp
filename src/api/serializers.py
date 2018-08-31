from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from rest_framework.validators import UniqueValidator

from src.blog.models  import Post, Comment
from src.base.models  import Carousel, CarouselImage, Site
from src.user.models import Profile
from src.services.models import Service
from src.ventas.models import Photo, Line, SubLine, Color, \
    Type, Provider, Brands, Department, Category, Article


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        max_length=32,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(min_length=8, write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'],
             validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        # fields = '__all__'


class SiteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Site
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = '__all__'


class BrandsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Brands
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

    def create(self, validated_data):
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.save()
        return instance

    class Meta:
        model = Article
        fields = '__all__'


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = '__all__'


class PhotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Photo
        fields = '__all__'


class LineSerializer(serializers.ModelSerializer):

    class Meta:
        model = Line
        fields = '__all__'


class SubLineSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubLine
        fields = '__all__'


class ColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Color
        fields = '__all__'


class TypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Type
        fields = '__all__'


class ProviderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Provider
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Group
        fields = '__all__'
        # fields = ('url', 'name')


class BlogPostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = '__all__'
        # fields = (
        #     'author','updated_by','title','sub_title',
        #     'text','draft','published','updated','created_at',
        #     'img','background','slug',
        # )


class BlogPostCommentsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = '__all__'


class FrontendCarouselSerializer(serializers.ModelSerializer):

    page = serializers.PrimaryKeyRelatedField( read_only=True )
    position = serializers.PrimaryKeyRelatedField( read_only=True )
    images = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Carousel
        fields = '__all__'
        # fields = ('name','description','page','position','crated_at','images',)


class FrontendCarouselImageSerializer(serializers.ModelSerializer):

    call_to_action_url = serializers.PrimaryKeyRelatedField( read_only=True)

    class Meta:
        model = CarouselImage
        # fields = ('image','name','text','call_to_action_url','uploaded_at')
        # fields = '__all__'
        exclude = (('call_to_action_url'),)


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
        exclude = ('groups','user_permissions')