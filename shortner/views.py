from django.shortcuts import render, redirect
import uuid
from .models import Url
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'index.html')

def create(request):
    if request.method=='POST':
        link=request.POST['link']#we are storing the link into link variable after the ajax updating ajax fn
        uid=str(uuid.uuid4())[:5] #unique id is allocated to the different string and it is of the length 5
        new_url=Url(link=link,uuid=uid)
        new_url.save()
        return HttpResponse(uid)
    
def go(request,pk):
    #first in urls.py another path is added for pk and go function is called
    url_details=Url.objects.get(uuid=pk)
    return redirect('https://'+url_details.link)