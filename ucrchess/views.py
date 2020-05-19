from django.shortcuts import render
from ucrchess.models import TestModel

def home(request):
    objs = TestModel.objects.all()
    return render(request, "home.html", {'objdata': objs})
