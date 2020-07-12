from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
def summarizeResult(request):
    #summarize whole_txt.txt and make summary.txt
    return redirect(to='/result/')