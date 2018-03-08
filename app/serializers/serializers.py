from django.contrib.auth.models import User, Group
from rest_framework import serializers

from src.blog.models  import Post, Comment
from src.base.models  import Carousel, CarouselImage


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = (
            'url', 'username', 'email', 'groups', 'is_superuser', 'is_active'
        )


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class BlogPostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('author','updated_by','title','sub_title',\
            'text','draft','published','updated','created_at',\
            'img','background','slug',
        )


class BlogPostCommentsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ('author','content','parent','approved','timestamp',\
            'post','object_id',
        )


class FrontendCarouselSerializer(serializers.ModelSerializer):

    page = serializers.PrimaryKeyRelatedField( read_only=True )
    position = serializers.PrimaryKeyRelatedField( read_only=True )
    images = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Carousel
        fields = ('name','description','page','position','crated_at','images',)


class FrontendCarouselImageSerializer(serializers.ModelSerializer):

    call_to_action_url = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = CarouselImage
        fields = ('image','name','text','call_to_action_url','uploaded_at')