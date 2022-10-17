from django.shortcuts import redirect, render
from .forms import StudentForm
from .scrape import Scrape
from codeforces import scrape
import webbrowser
# Create your views here.
def sayhello(request):
    student = StudentForm()
    if request.method == 'POST':
        uid = request.POST['id']
        sc = Scrape(uid)
        if sc.done == True:
            return redirect('/codeforces/data/')
    
    return render(request,"index.html",{'form':student})  