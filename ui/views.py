from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def sendResponse(request):
    return render(request,'result.html')