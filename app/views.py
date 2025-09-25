from django.shortcuts import render, get_object_or_404,redirect
from .models import Event

# Create your views here.
def event_form(request):
    last_event=Event.objects.last()
    if request.method =="POST":
        username=request.POST["Username"]
        email=request.POST["email"]
        password=request.POST["password"]
        location=request.POST["location"]
        time=request.POST["time"]
        date=request.POST["date"]
        image=request.FILES.get("image")
        event_info=Event(username=username, email=email, password=password, location=location, date=date,time=time, image=image)
        event_info.save()
        return redirect('event_details', event_id=event_info.id)
    # else:
    #     print("request not sent")
    return render(request, "index.html", {'last_event':last_event})

def event_details(request, event_id):
    event= get_object_or_404(Event, id=event_id)
    return render(request, "class.html", {'event':event})
