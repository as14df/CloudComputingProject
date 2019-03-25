from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.http import HttpResponseRedirect

#from .models import dict_ge_en
#from .forms import *

# TODO Impord er Code Snippets für die Google Translation
#from .google_translate_snippets import *

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")