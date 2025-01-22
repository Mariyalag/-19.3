from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Game, Buyer
from .models import News


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    # Настройка фильтрации по полям size и cost
    list_filter = ('size', 'cost')

    # Отображение полей title, cost и size
    list_display = ('title', 'cost', 'size')

    # Поиск по полю title
    search_fields = ('title',)

    # Ограничение кол-ва записей до 20
    list_per_page = 20


@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    # Настройка фильтрации по полям balance и age
    list_filter = ('balance', 'age')

    # Отображение полей name, balance и age
    list_display = ('name', 'balance', 'age')

    # Поиск по полю name
    search_fields = ('name',)

    # Ограничение кол-ва записей до 30
    list_per_page = 30

    # Доступным только для чтения поле balance
    readonly_fields = ('balance',)


admin.site.register(News)

# @admin.register(News)
# class NewsAdmin(admin.ModelAdmin):
#     list_display = ('title', 'category', 'created_at', 'is_published') #поля для отображения
#     list_filter = ('category', 'is_published') # фильтрация по категории и статусу публикации
#     search_fields = ('title', 'content') # поля для поиска
#     list_per_page = 30 # количество новостей на странице
#
# # разбиение полей на секции
#     fields = (
#         (None, {
#             'fields': ('title', 'content', 'category')
#         }),
#         ('Дополнительные настройки', {
#             'classes': ('collapse',), #скрытые секции по умолчанию
#             'fieids': ('is_published', 'created_at', 'updated_at')
#         })
#     )
#
#     readonly_fields = ('created_at', 'updated_at') # только для чтения полей


# { % extends
# 'task1/menu.html' %}
# { % block
# pagename %} < h1 > Игры < / h1 > { % endblock %}
# { % block
# menu %}{{block.super}}
# { % endblock %}
# { % block
# content %}
# < hr >
# { %
# for new in news %}
# < h2 > {{new.title}} < / h2 >
# < br >
# {{new.content}}
# < br >
# < small
# style = "float: right; margin-right: 20px;" > {{new.date}} < / small >
# < hr >
# { % endfor %}
#
# < div
#
#
# class ="pagination" >
#
# < span
#
#
# class ="step-links" >
#
#
# { % if news.has_previous %}
# < a
# href = "?page=1" > & laquo;
# Первая < / a >
# < a
# href = "?page={{ news.previous_page_number }}" > Предыдущая < / a >
# { % endif %}
#
# < span
#
#
# class ="current" >
#
#
# Страница
# {{news.number}}
# из
# {{news.paginator.num_pages}}.
# < / span >
#
# { % if news.has_next %}
# < a
# href = "?page={{ news.next_page_number }}" > Следующая < / a >
# < a
# href = "?page={{ news.paginator.num_pages }}" > Последняя & raquo; < / a >
# { % endif %}
# < / span >
# < / div >
# { % endblock %}