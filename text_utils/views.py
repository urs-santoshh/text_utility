#this file is created by urs-santoshh

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "index.html") 

def analyze(request):
    djtext = request.GET.get("text","default")
    removepunc = request.GET.get("removepunc","off")
    uppercase = request.GET.get("uppercase","off")
    newlineremover = request.GET.get("newlineremover","off")
    xtraspaceremover = request.GET.get("xtraspaceremover","off")
    parameter ={"purpose":"","analyzed_text":""}

    if removepunc =="on":
        punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punc:
                analyzed += char
        parameter["purpose"] = "removepunc "
        parameter["analyzed_text"] = analyzed
        djtext = analyzed
    
    if uppercase == "on":
        analyzed = djtext.upper()
        parameter["purpose"] += "uppercase "
        parameter["analyzed_text"] = analyzed
        djtext = analyzed

    if newlineremover == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed += char
        parameter["purpose"] += "newlineremover "
        parameter["analyzed_text"] = analyzed
        djtext = analyzed
        

    if xtraspaceremover == "on":
        analyzed = ""
        for index,char in enumerate(djtext):
            if djtext[index]==" " and djtext[index+1]== " ":
                pass
            else:
                analyzed += char
        parameter["purpose"] += "extraspaceremover "
        parameter["analyzed_text"] = analyzed
        
    if (removepunc !="on" and uppercase != "on" and newlineremover != "on" and xtraspaceremover != "on"):
        return HttpResponse("Error")

    return render(request,"analyze.html",parameter)
