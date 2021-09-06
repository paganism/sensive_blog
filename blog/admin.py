from django.contrib import admin
from blog.models import Post, Tag, Comment


class PostAdmin(admin.ModelAdmin):
    raw_id_fields = ('tags', 'likes', 'author', )


admin.site.register(Post, PostAdmin)

admin.site.register(Tag)


class CommentAdmin(admin.ModelAdmin):
    raw_id_fields = ('post', 'author', )


admin.site.register(Comment, CommentAdmin)
