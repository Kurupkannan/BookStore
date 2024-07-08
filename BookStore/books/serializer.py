from rest_framework import serializers
from .models import  Book
from authors.models import Author

class BookSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())

    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'published_date', 'genre')

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['author'] = instance.author.name if instance.author else None
        return representation
