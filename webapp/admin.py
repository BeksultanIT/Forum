from django.contrib import admin

from webapp.models.forums import Forum


# Register your models here.
class ForumAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at','updated_at')

admin.site.register(Forum, ForumAdmin)