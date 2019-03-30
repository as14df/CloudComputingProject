from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views import generic
from django.views.decorators.csrf import csrf_exempt,csrf_protect

#from .models import dict_ge_en
#from .forms import *

# TODO Impord er Code Snippets für die Google Translation
#from .google_translate_snippets import *

from .models import GuiInfo, Ger_Eng_Dict

@csrf_exempt
def index(request):

    trans = GuiInfo(german = "", english = "")

    trans.fromLang = request.POST.get("fromLang", "Deutsch")
    trans.toLang = request.POST.get("toLang", "Englisch")

    msg1 = request.POST.get("msg1", "");

    if 'translate' in request.POST:
        if msg1 != "":
            trans.german = msg1
            translation = Ger_Eng_Dict.objects.get(german = msg1)
            trans.english = translation.english
    elif 'changeLang' in request.POST:
        b = trans.toLang
        trans.toLang = trans.fromLang
        trans.fromLang = b;

    return render(request, 'speaker/index.html', {'trans': trans})