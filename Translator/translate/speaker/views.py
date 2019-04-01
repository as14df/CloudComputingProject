from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views import generic
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from google.cloud import translate
#from .models import dict_ge_en
#from .forms import *

# TODO Impord er Code Snippets für die Google Translation
#from .google_translate_snippets import *

from .models import GuiInfo, Ger_Eng_Dict

@csrf_exempt
def index(request):
    trans = GuiInfo(msg1 = "", msg2 = "")

    trans.fromLang = request.POST.get("fromLang", "Deutsch")
    trans.toLang = request.POST.get("toLang", "Englisch")

    msg1 = request.POST.get("msg1", "");

    if 'translate' in request.POST:
        if msg1 != "":
            try:
                if trans.fromLang == "Deutsch":
                    trans.msg1 = msg1
                    translation = Ger_Eng_Dict.objects.get(german = msg1)
                    trans.msg2 = translation.english
                else:
                    trans.msg1 = msg1
                    translation = Ger_Eng_Dict.objects.get(english = msg1)
                    trans.msg2 = translation.german
            except Exception as e:
                translate_client = translate.Client() 
                translation = ""

                if trans.fromLang == "Deutsch":
                    translation = translate_client.translate(msg1, target_language='en')
                    obj = Ger_Eng_Dict(german=msg1, english=translation['translatedText'])
                    
                else:
                    translation = translate_client.translate(msg1, target_language='ger')
                    obj = Ger_Eng_Dict(german=translation['translatedText'], english=msg1)

                obj.save()
                trans.msg2 = translation['translatedText']                            
    elif 'changeLang' in request.POST:
        b = trans.toLang
        trans.toLang = trans.fromLang
        trans.fromLang = b;

    return render(request, 'speaker/index.html', {'trans': trans})

def about(request):

    return render(request, 'speaker/about.html', None)

