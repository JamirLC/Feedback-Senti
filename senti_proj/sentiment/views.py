from django.shortcuts import render

# Create your views here.
# View for the homepage
def home(request):
    return render(request, 'sentiment/home.html')

# View for the sentiment analysis page
def admin(request):
    return render(request, 'sentiment/admin.html')

def generate(request):
    return render(request, 'sentiment/generate.html')



# Views for the events (event1, event2, etc.)
def event_1(request):
    return render(request, 'events/event1.html')

def event_2(request):
    return render(request, 'events/event2.html')

def event_3(request):
    return render(request, 'events/event3.html')

def event_4(request):
    return render(request, 'events/event4.html')
