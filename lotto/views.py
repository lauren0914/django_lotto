from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import GuessNumbers
from .forms import PostForm

def index(request):

    lottos = GuessNumbers.objects.all()
                # class 기반으로 만들어진 모든 붕어빵 꺼내
    return render(request, 'lotto/default.html', {'lottos' : lottos})
    # 사용자 request, html파일경로, context-dict

def post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            lotto = form.save(commit=False)
            lotto.generate()
            return redirect('index')
    else :
        form = PostForm()
        return render(request, 'lotto/form.html', {'form':form})

def detail(request, lottokey):

    lotto = GuessNumbers.objects.get(id=lottokey)
    return render(request, 'lotto/detail.html', {'lotto':lotto})
def hello(request):
    return HttpResponse('<h1 style="color:red;">Hello, world!</h1>')
