from word.models import Word


class WordValidator:
    @classmethod
    def word(cls, word: str) -> None:
        word = Word.objects.filter(word=word)

        if not word:
            return False

        try:
            str(word)
        except ValueError:
            return False
        return True

