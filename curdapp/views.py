from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from curdapp.models import StudentData


def test(request):
    return HttpResponse("Hello how are you")


def home_page(request):

    students = StudentData.objects.all()
    return render(request, 'homepage.html', {'students': students})
    pass

