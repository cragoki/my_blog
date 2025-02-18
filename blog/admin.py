from django.contrib import admin

from blog.models import Post, Author, Tag




class PostAdmin(admin.ModelAdmin):
    list_filter = ('author', 'date', 'tags')
    list_display = ('title', 'author', 'date')
    prepopulated_fields = {'slug': ('title',)}

# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)