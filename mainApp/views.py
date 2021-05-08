from django.shortcuts import render


def index(request):
    return render(request, 'mainApp/homepage.html')


def contacts(request):
    return render(request,
                  'mainApp/basic.html',
                  {'values':
                       ['Если у вас остались вопросы, задавайте '
                        'их по телефону',
                        '8(044)-758-18-66',
                        'coromilly@gmail.com',]
                   }
                  )
