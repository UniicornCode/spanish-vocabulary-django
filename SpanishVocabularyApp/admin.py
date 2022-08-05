from django.contrib import admin

# Register your models here.
from SpanishVocabularyApp.models import City, Category, Word


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)


class WordAdmin(admin.ModelAdmin):
    list_display = ("spanish",)


#class AnswerInline(admin.TabularInline):
#    model = Answer
#
#
#class QuestionAdmin(admin.ModelAdmin):
#    inlines = [AnswerInline]
#
#
#admin.site.register(Question, QuestionAdmin)
#admin.site.register(Answer)
admin.site.register(City)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Word, WordAdmin)
