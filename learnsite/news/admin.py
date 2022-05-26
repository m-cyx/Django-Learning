from django.contrib import admin

# Register your models here.
# Тут регистрируем модели для админки
from .models import News
from .models import Category


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at',
                    'updated_at', 'is_published', 'category') # Какие поля оттображать в списке 
    list_display_links = ('id', 'title') # Какие поля являются ссылкой
    search_fields = ('title', 'content', 'category') # По каким полям можно искать
    list_editable = ('is_published',) # Какие поля можно редактировать из админики 
    list_filter = ('is_published', 'category') # По каким полям фильтруем


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
