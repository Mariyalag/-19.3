from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Game, Buyer


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