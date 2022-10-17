import email
from django.shortcuts import render
from django.http import HttpResponse
from .forms import SnippitForm
# Create your views here.

# def contact(request):
    
#     if request.method == 'POST':
#         form = Contactform(request.POST)
#         if form.is_valid():
            
#             name = form.cleaned_data['name']
#             email = form.cleaned_data['email']
            
#             print(name)
    
#     form = Contactform()# to clear form remove the else and le he command run all time and to rediredt to thanks page you can use it.
    
#     return render(request, 'form.html', {'form' : form})

def snippet_detail(request):
    if request.method == 'POST':
        form = SnippitForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form.save()
            
    
    form = SnippitForm()
    
    return render(request, 'form.html', {'form' : form})


def index(request):
    return render(request, 'index.html')