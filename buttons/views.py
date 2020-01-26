from django.shortcuts import render

from .button_functions import say_hi_in_terminal

def buttons_home_view(request):
    if request.method == "POST":
        say_hi_in_terminal()
    return render(request, 'buttons/buttons_home.html')
