from django.contrib import admin

from .models import (Question, Choice)

admin.site.site_header = 'Poll App Admin'
admin.site.site_title = 'Poll App Admin Area'
admin.site.index_title = 'Welcome to the Poll App Admin Area'

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldSets = [(None, {'fields' : ['question_text']}),
                ('Date Information', {'fields':['publish_date'],
                'classes' : ['collapse']}),]
    inlines = [ChoiceInLine]
admin.site.register(Question, QuestionAdmin)
