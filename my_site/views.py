from django.shortcuts import render
from django.http import HttpResponse

'''Return the index.html page to be displayed.
'''
# Create your views here.
def index(request):
    return render(request, "index.html")