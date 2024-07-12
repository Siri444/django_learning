from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .forms import bookingform
from .models import menu

def home(request):
    return render(request,'header.html')
def Menu(request):
    menu_items=menu.objects.all()
    main_data={'menu':menu_items}
    return render(request,'menu.html',{'menu':main_data})
    
def booking(request):
    submitted=False
    if request.method == 'POST':
        form = bookingform(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/book?submitted=True')
    else:
        form=bookingform
        if 'submitted' in request.GET:
            submitted=True
    return render(request,'book.html',{'form':form,'submitted':submitted})