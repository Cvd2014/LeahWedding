from django.shortcuts import render
from models import Bride, Groom, Party

# Create your views here.

def get_index(request):
     brides=Bride.objects.filter()
     bride=brides[0]
     grooms=Groom.objects.filter()
     groom=grooms[0]
     party=Party.objects.filter()

     return render(request, 'homepage.html',{'bride':bride,'groom':groom,'party':party})