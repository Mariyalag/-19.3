from django.urls import path
from .views import sign_up_by_django, sign_up_by_html, home, cards, contact, testimonials, blog, game_list, news

urlpatterns = [
    path('django_sign_up/', sign_up_by_html, name='sign_up_html'),
    path('', sign_up_by_django, name='sign_up_django'),
    path('home/', home, name='home'),
    path('cards/', cards, name='cards'),
    path('contact/', contact, name='contact'),
    path('testimonials/', testimonials, name='testimonials'),
    path('blog/', blog, name='blog'),
    path('home/games/', game_list, name='game_list'),
    path('registration/', sign_up_by_html, name='registration'),
    path('news/', news, name='news'),
]
