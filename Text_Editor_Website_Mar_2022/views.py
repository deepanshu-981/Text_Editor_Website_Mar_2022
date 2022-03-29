from django.http import HttpResponse
from django.shortcuts import render
# def index(request):
#     return HttpResponse('''Harry  Django CodeWithHarry''')
# python manage.py runserver
def index(request):
    return render(request, 'index.html')

def analyze(request):
    #Get the text
    text=""
    naam = request.GET.get('name', 'default')
    mail = request.GET.get('mail', 'default')
    djtext = request.GET.get('text', 'default')
    analyzed=""
    f=0
    removepunc=request.GET.get('removepunc','off')
    cap=request.GET.get('capitalize','off')
    lower=request.GET.get('lower','off')
    if removepunc == "on":
        if(text!=""):
            text+=", "
        text+="Removing Punctuations";
        f=1
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~+-*/.=_'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
    if cap == "on":
        if(text!=""):
            text+=", "
        text+="Capitalize Full"
        if f==1:
            analyzed = analyzed.upper()
        else:
            f=1
            analyzed = djtext.upper()
    if lower == "on":
        if(text!=""):
            text+=", "
        text+="Lowercase Full"
        if f==1:
            analyzed = analyzed.lower()
        else:
            f=1
            analyzed = djtext.lower()
    elif(f==0):

        return HttpResponse('You have not selected any operation')
    
    para = {'purpose': text, 'analyzed_text': analyzed,'original': djtext,'name':naam,'mail':mail}
    return render(request,'analyze.html',para)
