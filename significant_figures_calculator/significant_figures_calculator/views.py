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

#object尾 O 是指Significant_figures物件
def acceleration(request):
    if request.POST:
        dot = request.POST.get('dot', '')
        sub_time_reciprocalO = Significant_figures(str(60/int(dot)))
        position = request.POST.getlist('position')
        positionO = []                      #位置
        positionJ = []                      
        for i in position:
            positionO.append(Significant_figures(i))
            positionJ.append(export_in_javascript_object_form(positionO[-1]))
        displacementO = []                  #位移
        displacementJ = []                  
        for i in range(len(position) - 1):
            displacementO.append(positionO[i + 1] - positionO[i])
            displacementJ.append(export_in_javascript_object_form(displacementO[-1]))
        velocityO = []                      #速度
        velocityJ = []                      
        for i in displacementO:
            velocityO.append(i * sub_time_reciprocalO)
            velocityJ.append(export_in_javascript_object_form(velocityO[-1]))
        change_velocityO = []               #速度變化量
        change_velocityJ = []
        for i in range(len(velocityO) - 1):
            change_velocityO.append(velocityO[i + 1] - velocityO[i])
            change_velocityJ.append(export_in_javascript_object_form(change_velocityO[-1]))
        accelerationO = []                  #加速度
        accelerationJ = []
        for i in change_velocityO:          
            accelerationO.append(i * sub_time_reciprocalO)
            accelerationJ.append(export_in_javascript_object_form(accelerationO[-1]))
        quantity = len(accelerationJ)
        sum_accelerationO = Significant_figures("0.00")
        for i in accelerationO:
            sum_accelerationO = sum_accelerationO + i
        average_accelerationO = sum_accelerationO * Significant_figures(str(1/len(accelerationO)))
        average_accelerationJ = export_in_javascript_object_form(average_accelerationO)
        return render(request, 'acceleration_output.html', locals())
    else:
        return render(request, 'acceleration_input.html', locals())

        
