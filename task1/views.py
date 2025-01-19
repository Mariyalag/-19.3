from django.shortcuts import render

# Create your views here.
# from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .forms import UserRegister
from .models import Buyer, Game





def home(request):
    return render(request, 'fourth_task/home.html')



def cards(request):
    cards_info = {
        'past': 'Карта прошлого помогает понять, какие события и эмоции повлияли на ваше текущее состояние',
        'present': 'Карта настоящего позволяет осознать текущие чувства и ситуации, в которых вы находитесь',
        'future': 'Карта будущего открывает перспективы и возможности, которые могут появиться в вашей жизни'
    }
    return render(request, 'fourth_task/cards.html', {'cards_info': cards_info})


def contact(request):
    return render(request, 'fourth_task/contact.html')



def testimonials(request):
    testimonials_list = [
        "<i>Отличный опыт! Помогли разобраться в своих чувствах.</i>",
        "<i>Очень профессионально и внимательно. Рекомендую!</i>",
        "<i>МАК-карты открыли мне глаза на многие вещи.</i>"
    ]
    return render(request, 'fourth_task/testimonials.html', {'testimonials': testimonials_list})


def blog(request):
    articles = [
        {
            "title": "Как МАК-карты помогают в психологии",
            "content": (
                "<p>МАК-карты (метафорические ассоциативные карты) — это эффективный инструмент в психологии, "
                "который помогает людям лучше понять свои чувства, переживания и внутренние конфликты.</p>"
                "<p>Они представляют собой набор карт с изображениями, символами или словами, которые вызывают "
                "ассоциации и эмоции. Вот несколько способов, как МАК-карты могут быть полезны в психологии:</p>"
                "<ol>"
                "<li><strong>Самовыражение:</strong> МАК-карты позволяют клиентам выразить свои мысли и чувства, "
                "которые часто трудно verbalizovat. Это особенно полезно для людей, испытывающих трудности в "
                "коммуникации.</li>"
                "<li><strong>Углубленное понимание:</strong> Использование карт помогает выявить скрытые аспекты "
                "личности и внутренние конфликты, что способствует более глубокому самопознанию.</li>"
                "<li><strong>Процесс терапии:</strong> В сессиях с психологом карты могут служить отправной точкой "
                "для обсуждения, помогая клиентам открыться и углубиться в свои переживания.</li>"
                "<li><strong>Работа с метафорами:</strong> МАК-карты активно используют метафоры, что позволяет "
                "клиентам переосмыслить свои проблемы и найти новые решения.</li>"
                "<li><strong>Креативный подход:</strong> Этот инструмент делает процесс терапии более увлекательным "
                "и менее формальным, что может снизить уровень тревожности у клиентов.</li>"
                "</ol>"
                "<p>Таким образом, МАК-карты являются мощным средством для самопознания и развития, "
                "помогая людям открывать новые горизонты в понимании себя и своих эмоций.</p>"
            )
        },
        {
            "title": "5 советов по саморазвитию",
            "content": (
                "<ol>"
                "<li><strong>Постановка целей:</strong> Определите краткосрочные и долгосрочные цели. Записывайте "
                "их и регулярно отслеживайте прогресс.</li>"
                "<li><strong>Чтение и обучение:</strong> Регулярно читайте книги, статьи и проходите курсы по "
                "интересующим вас темам для расширения кругозора и повышения квалификации.</li>"
                "<li><strong>Рефлексия:</strong> Проводите время на самоанализ. Оценивайте свои достижения, ошибки "
                "и уроки, которые вы из них извлекли.</li>"
                "<li><strong>Практика новых навыков:</strong> Применяйте на практике то, что изучили. Регулярная "
                "практика помогает закрепить знание и развить уверенность в себе.</li>"
                "<li><strong>Забота о здоровье:</strong> Поддерживайте физическое и психическое здоровье через "
                "регулярные физические нагрузки, здоровое питание и достаточный сон. Здоровье — основа для "
                "успешного саморазвития.</li>"
                "</ol>"
            )
        },
    ]
    return render(request, 'fourth_task/blog.html', {'articles': articles})



users = ['user1', 'user2', 'user3']


def sign_up_by_django(request):
    info = {}
    form = UserRegister(request.POST or None)

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age', 0))


        existing_users = Buyer.objects.all()
        usernames = [buyer.name for buyer in existing_users]


        if username in usernames:
            info['error'] = 'Пользователь уже существует'
        elif age < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        else:
            # users.append(username)
            Buyer.objects.create(name=username, balance=0.00, age=age)
            info['message'] = f'Приветствуем, {username}! Вы успешно зарегистрированы.'
            return redirect('home')

    info['form'] = form
    return render(request, 'fifth_task/registration_page.html', context=info)


def sign_up_by_html(request):
    info = {}
    form = UserRegister(request.POST or None)

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age', 0))

        existing_users = Buyer.objects.all()
        usernames = [buyer.name for buyer in existing_users]

        if username in usernames:
            info['error'] = 'Пользователь уже существует'
        elif age < 18:
            info['error'] = 'Вы должны быть старше 18'
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        else:
            Buyer.objects.create(name=username, balance=0.00, age=age)
            info['message'] = f'Приветствуем, {username}! Вы успешно зарегистрированы.'
            return redirect('home')

    info['form'] = form
    return render(request, 'fifth_task/registration_page.html', context=info)

def game_list(request):
    games = Game.objects.all()
    return render(request, 'fourth_task/game_list.html', {'games': games})
