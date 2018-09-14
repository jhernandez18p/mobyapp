from django.contrib import admin

from src.faq.models import Question, Answer

class AnswerInline(admin.StackedInline):
    model = Answer
    extra = 1


class QuestionModelAdmin(admin.ModelAdmin):
    list_display = ['title',]
    inlines = [AnswerInline,]

    class Meta:
        model = Question


admin.site.register(Question, QuestionModelAdmin)
