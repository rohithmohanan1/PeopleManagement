from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from django.contrib.auth.decorators import login_required
from .models import Person
from .forms import PersonForm
# Create your views here.

def add(request):
    context = {}
    form = PersonForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/')
    context['form'] = form
    return render(request, 'index.html', context)

def list(request):
    context ={}
    context["dataset"] = Person.objects.all()     
    return render(request, "list.html", context)

def detail(request, id):
    context ={}
    context["data"] = Person.objects.get(id = id)        
    return render(request, "detail.html", context)

# @login_required
def update(request, id):
    context ={}
    obj = get_object_or_404(Person, id = id)
    form = PersonForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)
    context["form"] = form
    return render(request, "update.html", context)

def delete(request, id):
    context ={}
    obj = get_object_or_404(Person, id = id) 
    if request.method =="POST":
        obj.delete()
        return HttpResponseRedirect("/")
    return render(request, "delete.html", context)



# some comments 