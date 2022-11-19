from django.shortcuts import render


def home(request):
    return render(request, "money_manage/index.html", context={
        'ola': "Olá Mundo"
    })
