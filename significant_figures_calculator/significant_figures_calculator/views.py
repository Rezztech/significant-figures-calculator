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

#def add(request):
    
