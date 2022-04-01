from django.contrib import admin
from .models import Tag, Post, Author, Comment

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_filter = ("author", "tag", "date", )
    list_display = ("title", "author", "date", )
    prepopulated_fields = {"slug": ("title", )}

class CommentAdmin(admin.ModelAdmin):
    list_display = ("user_name", "post")


admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Comment, CommentAdmin)
