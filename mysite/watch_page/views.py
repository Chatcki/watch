from django.shortcuts import render

def watch_page(request):
    context={}
    template='watch_page/watch.html'
    return render(request,template,context)
