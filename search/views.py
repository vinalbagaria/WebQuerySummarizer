from django.shortcuts import render
from django.shortcuts import redirect
from ui.forms import NameForm
# Create your views here.
def searchQuery(request):
    #search query and get links on the first page
    #prepare links.txt file and save it
    form = NameForm(request.POST)
    print("test1")
    # check whether it's valid:
    if form.is_valid():
        query = form.cleaned_data['queryy']
        print(query)

        # redirect to a new URL:
        return redirect(to='/scrape/'+query)