from django.shortcuts import render
from .forms import StudentForm
from .scrape import Scrape
# Create your views here.
def sayhello(request):
    student = StudentForm()
    if request.method == 'POST':
        uid = request.POST['id']
        sc = Scrape(uid)
    return render(request,"index.html",{'form':student})  