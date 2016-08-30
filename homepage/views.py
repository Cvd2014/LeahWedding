from django.shortcuts import render
from models import Bride, Groom, Party,Venue

# Create your views here.

def get_index(request):
     brides=Bride.objects.filter()
     bride=brides[0]
     grooms=Groom.objects.filter()
     groom=grooms[0]
     party=Party.objects.filter()
     venues=Venue.objects.filter()

     return render(request, 'homepage.html',{'bride':bride,'groom':groom,'party':party,'venues':venues})