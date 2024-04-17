from django.shortcuts import render, redirect
from .models import Event
from .forms import BookingForm

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def events(request):
    events = Event.objects.all()
    return render(request, 'events.html', {'events': events})

def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = BookingForm()
    return render(request, 'booking.html', {'form': form})

def contact(request):
    return render(request, 'contact.html')

from django.shortcuts import render

def about(request):
    return render(request, 'about.html')

