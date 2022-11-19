from django.shortcuts import render


def home(request):
    return render(request, "money_manage/pages/index.html", context={
        'ola': "Olá Mundo"
    })
