from django.contrib import admin

from .models import Category, Recipe

class CategoryAdmin(admin.ModelAdmin):
    ...

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'created_at', 'updated_at')
    search_fields = ('author__username', 'title', 'description', 'id')
    list_filter = ('author__username', 'created_at', 'updated_at')
    list_per_page = 10
    ordering = ('-created_at',)
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Recipe, RecipeAdmin)