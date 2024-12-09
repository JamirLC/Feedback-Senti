from django.shortcuts import render
from django.shortcuts import render
from .models import Sentiment
from rest_framework.views import APIView
from rest_framework.response import Response
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
from django.db.models import Count

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


model = AutoModelForSequenceClassification.from_pretrained(r'D:\VSCODE\Feedback-Senti\model\taglish')
tokenizer = AutoTokenizer.from_pretrained(r'D:\VSCODE\Feedback-Senti\model\taglish')
sentiment_pipeline = pipeline('sentiment-analysis', model=model, tokenizer=tokenizer)


class SentimentAnalysisView(APIView):
    def post(self, request, *args, **kwargs):
        text = request.data.get("text")
        if not text:
            return Response({"error": "No text provided"}, status=400)
        
        result = sentiment_pipeline(text)
        sentiment_label = result[0]["label"]
        sentiment_score = result[0]["score"]


        if sentiment_label == "LABEL_0":
            sentiment = "Negative"
        elif sentiment_label == "LABEL_2":
            sentiment = "Positive"
        else:
            sentiment = "Neutral"

        feedback = Sentiment.objects.create(
            event="Feedback",
            text=text,
            sentiment=sentiment,
            created_at=None
        )

        

        return Response({
            "sentiment": sentiment,
            "score": sentiment_score
        }, status=200)


class SentimentListView(APIView):
    def get(self, request, *args, **kwargs):
        sentiments = Sentiment.objects.all()
        
        # Count sentiments
        sentiment_counts = Sentiment.objects.values('sentiment').annotate(count=Count('sentiment'))
        sentiment_summary = {item['sentiment']: item['count'] for item in sentiment_counts}

        data = {
            "sentiments": [
                {
                    "id": sentiment.id,
                    "event": sentiment.event,
                    "text": sentiment.text,
                    "sentiment": sentiment.sentiment,
                    "created_at": sentiment.created_at
                }
                for sentiment in sentiments
            ],
            "summary": sentiment_summary
        }
        return Response(data)
