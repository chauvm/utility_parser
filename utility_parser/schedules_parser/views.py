from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
	msg = "Schedules Parser App"
	context = {"msg" : msg}
	return render(request, "schedules_parser/index.html", context)
	
def ice_rink(request):
	return HttpResponse("Veteran Ice Rink Schedule")