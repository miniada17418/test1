from django.shortcuts import render

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    return render(request,'accounts/index.html')

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password =  request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))

            else:
                return HttpResponse('Account Not Active.  See Your Manager to Gain Access.')

        else:
            print("someone tried to login and failed")
            print('Username: {} and Password: {}'.format(username,password))
            return HttpResponse("Invalid login details supplied!")

    else:
        return render(request, 'accounts/login.html', {})
