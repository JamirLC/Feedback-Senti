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