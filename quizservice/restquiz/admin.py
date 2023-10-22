from django.contrib import admin

from restquiz.models import Categoryes, Quiz

@admin.register(Categoryes)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    search_fields = ('title',)
    list_filter = (
        "title",
    )

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    list_display = ('id', 'category',)
    search_fields = ('category',)
    list_filter = (
        "category",
    )
