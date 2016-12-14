from django.contrib import admin

from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3


class QuestionAdmin(admin.ModelAdmin):
	# fields = ['pub_date', 'question_text']
	list_display = ('question_text', 'pub_date', 'was_published_recently')
	fieldsets = [
		('Question Registraion', {'fields': ['question_text']}),
		('Data information', {'fields' : ['pub_date']}),
	]
	inlines = [ChoiceInline]
	# list_filter = ['pub_date']
	list_filter = ['pub_date', 'question_text']
	search_fields = ['pub_date']

admin.site.register(Question, QuestionAdmin)

admin.site.register(Choice)