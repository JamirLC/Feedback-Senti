from django.shortcuts import render
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification

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


model = AutoModelForSequenceClassification.from_pretrained('C:\Users\ACER\Desktop\Web\lavalust\Feedback-Senti\senti_proj\sentiment\model')
tokenizer = AutoTokenizer.from_pretrained('C:\Users\ACER\Desktop\Web\lavalust\Feedback-Senti\senti_proj\sentiment\model')

sentiment_pipeline = pipeline('sentiment-analysis', model=model, tokenizer=tokenizer)


class SentimentAnalysisView(APIView):
    def post(self, request, *args, **kwargs):
        text = request.data.get("text")
        if not text:
            return Response({"error": "No text provided"}, status=400)
        
        result = sentiment_pipeline(text)
        if result[0]["label"] == "LABEL_0":
            return Response({
                "sentiment": "Negative",
                "score": result[0]
            }, status=200)
        elif result[0]["label"] == "LABEL_2":
            return Response({
                "sentiment": "Positive",
                "score": result[0]
            }, status=200)
        else:
            return Response({
                "sentiment": "Neutral",
                "score": result[0]
            }, status=200)