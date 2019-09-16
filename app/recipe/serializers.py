from rest_framework import serializers

from core.models import Tag, ingredient


class TagSerializer(serializers.ModelSerializer):
    """ Serializer for Tag objects """

    class Meta:
        model = Tag
        fields = ('id', 'name')
        read_only_fields = ('id',)


class IngredientSerializer(serializers.ModelSerializer):
    """Serializer for an ingredient object"""

    class Meta:
        model = ingredient
        fields = ('id', 'name')
        read_only_fields = ('id',)
