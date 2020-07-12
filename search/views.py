from django.shortcuts import render
from django.shortcuts import redirect

# Create your views here.
def searchQuery(request):
    #search query and get links on the first page
    #prepare links.txt file and save it
    return redirect(to='/scrape/')