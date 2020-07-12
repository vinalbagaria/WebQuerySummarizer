from django.shortcuts import redirect

# Create your views here.
def scrapePages(request):
    #Scrape,clean and make whole_text.txt
    return redirect(to='/summarize/')