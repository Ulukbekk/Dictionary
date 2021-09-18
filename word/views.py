
from rest_framework import generics, permissions, status

from rest_framework.response import Response

from word.models import Word, Meaning
from word.serializers import MeaningSerializer, WordSerializer

# class RetrieveMeaningAPIView(generics.RetrieveAPIView):
#     serializer_class = MeaningSerializer
#     queryset = Word.objects.filter()
#     permission_classes = (permissions.AllowAny,)
#
#     def get(self, request, *args, **kwargs):
#         queryset = self.get_queryset()
#         serializer = MeaningSerializer(queryset, many=True)
#         return Response(serializer.data)
from word.validators import WordValidator


class WordRetrieveQPIView(generics.RetrieveAPIView):
    permission_classes = (permissions.AllowAny,)
    validator_class = WordValidator

    def get(self, request, *args, **kwargs):
        title = request.POST.get('word')
        if not self.validator_class.word(title):
            return Response('This word was not found', status=status.HTTP_412_PRECONDITION_FAILED)

        word_id = Word.objects.get(word=title).pk
        word = Word.objects.filter(id=word_id).first()
        meaning = Meaning.objects.filter(word=word)
        print(title)
        serializer = MeaningSerializer(meaning, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)





