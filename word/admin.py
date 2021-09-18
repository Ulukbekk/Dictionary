from django.contrib import admin

from word.models import Word, Meaning

admin.site.register(Word)
@admin.register(Meaning)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id',
                    "word",
                    )