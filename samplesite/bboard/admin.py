from django.contrib import admin

# Register your models here.

from .models import Bb, Rubric


class BbAdmin(admin.ModelAdmin):
    list_display = ('rubric', 'title', 'content', 'price', 'published',)
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content')
    readonly_fields = ('published',)


admin.site.register(Bb, BbAdmin)
admin.site.register(Rubric, )
