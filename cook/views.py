from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm

# 로그인, 로그아웃 함수는 이미 urlpatterns = [ path(‘accounts/’, include(‘django.contrib.auth.urls’)),]
#  이걸 사용함으로서 구현된 함수를 사용하면 되기에 signup만 정의해 주자
# 또한 필요한 템플릿은 login.html과 signup.html만 제대로 만들어 놓자.

# 회원가입 함수
def signup(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')

    else:
        form = SignUpForm()

    return render(request, 'registration/signup.html', {'form': form})