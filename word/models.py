from django.db import models


class Word(models.Model):
    word = models.CharField(max_length=50)

    def __str__(self):
        return self.word


class Meaning(models.Model):
    word = models.ForeignKey(Word, on_delete=models.CASCADE,
                             related_name='word_meaning')
    meaning = models.TextField()

    def __str__(self):
        return f'{self.word.word}, {self.meaning}'


