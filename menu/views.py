from django.shortcuts import render



def child(request):
    return render(request, 'menu/child.html')

def page1(request):
    return render(request, 'menu/page1.html')

def page2(request):
    return render(request, 'menu/page2.html')
