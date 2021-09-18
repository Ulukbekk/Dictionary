from rest_framework import serializers

from word.models import Meaning, Word


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ('id',
                  'word',)


class MeaningSerializer(serializers.ModelSerializer):
    words = WordSerializer(many=True, read_only=True)

    class Meta:
        model = Meaning
        fields = ('words',
                  'id',
                  'word',
                  'meaning')

