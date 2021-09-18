from django.urls import path

from word.views import WordRetrieveQPIView

urlpatterns = [
    # path('', RetrieveMeaningAPIView.as_view()),
    path('', WordRetrieveQPIView.as_view()),
]