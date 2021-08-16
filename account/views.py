from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def login(request):
    _next = request.GET.get('next', '/account/mine')
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth.login(request, form.get_user())
            return HttpResponseRedirect(_next)
    else:
        form = AuthenticationForm(request)

    content = {
        'form': form,
        'next': _next
    }
    return render(request, 'account/login.html', content)


@csrf_exempt
def mine(request):
    return HttpResponse('欢迎登录')
