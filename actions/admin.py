from django.contrib import admin
from .models import Like, Comment


class LikeAdmin(admin.ModelAdmin):
    list_display = ('liked_date',)


admin.site.register(Like, LikeAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('commented_date', 'user')


admin.site.register(Comment, CommentAdmin)
