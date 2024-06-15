from rest_framework import serializers
from .models import Blog


"""
 from blogs.serializers import BlogSerializer
>>> from blogs.models import Blog
>>> from rest_framework.renderers import JSONRenderer 
>>> new_blog = Blog(
... title = "Learn DRF",
... content = "Basics of DRF")
>>> new_blog.save()
>>> serializer = BlogSerializer(instance = new_blog)
>>> serializer
BlogSerializer(instance=<Blog: Learn DRF>):
    id = IntegerField(read_only=True)
    title = CharField(max_length=50)
    content = CharField()
    created = DateTimeField(read_only=True)
>>> serializer.data
{'id': 3, 'title': 'Learn DRF', 'content': 'Basics of DRF', 'created': '2024-05-29T07:48:00.521085Z'}
 
"""
# class BlogSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only = True)
#     title = serializers.CharField(max_length = 50)
#     content = serializers.CharField()
#     created = serializers.DateTimeField(read_only = True)

class BlogSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length = 50)
    class Meta:
        model= Blog
        fields = ["id", "title", "content", "created"]