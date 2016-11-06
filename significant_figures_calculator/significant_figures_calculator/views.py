from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .Significant_figures import *
from django import template

#   just demo how to get post in array
#   in HTML use <input name="position"><input name="position"><input name="position"><input name="position">
#   and in python use request.POST.getlist('position')
#def post_demo(request):
#    if request.POST:
#        ret = request.POST.getlist('position')
#        return HttpResponse(ret)
#    else:
#        return render(request,'post.html',locals())

def add(request):
    if request.POST:
        augend = request.POST.get('augend', '')
        addend = request.POST.get('addend', '')
        augendO = Significant_figures(augend)
        addendO = Significant_figures(addend)
        answerO = augendO + addendO
        augend = export_in_javascript_object_form(augendO)
        addend = export_in_javascript_object_form(addendO)
        answer = export_in_javascript_object_form(answerO)
        return render(request, 'add.html', locals())
    else:
        return render(request, 'add.html', locals())
