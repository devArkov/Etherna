from django.contrib import admin
from .models import Category, Tag, Author, Post
from django.utils.safestring import mark_safe


# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('id', 'title', 'preview', 'author', 'created_at', 'thumbnail')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'category', 'tag')
    list_filter = ('category',)
    readonly_fields = ('views', 'created_at')
    fields = ('title', 'slug', 'text', 'category', 'tags', 'photo', 'author', 'created_at', 'views')
    save_as = True
    save_on_top = True

    def thumbnail(self, object):
        if object.photo:
            return mark_safe(f'<img src="{object.photo.url}" width="100">')
        return mark_safe('<img src="/static/img/no_photo.jpg" width="100">')

    thumbnail.short_description = 'Photo'
