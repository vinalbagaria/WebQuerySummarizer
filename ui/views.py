from django.shortcuts import render, redirect
from .forms import NameForm

# Create your views here.
def index(request):
    form = NameForm()

    print("test0")
    return render(request, 'index.html', {'form': form})

def sendResponse(request):
    return render(request,'result.html')