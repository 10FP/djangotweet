from django.shortcuts import render, redirect
from . import models
from django.urls import reverse, reverse_lazy
from . import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView

# Create your views here.

def listtweet(request):
    all_tweets = models.Tweet.objects.all()
    tweet_dict = {"tweets": all_tweets}
    return render(request, "tweetapp/listtweet.html", context=tweet_dict)

@login_required(login_url="/login")
def addtweet(request):
    if request.POST:
        tweet = request.POST["tweet"]
        tweet = models.Tweet(username=request.user, tweet=tweet)
        tweet.save()
        return redirect(reverse("tweetapp:listtweet"))
    else:
        return render(request, "tweetapp/addtweet.html")


def addtweetbyform(request):
    if request.method == "POST":
        form = forms.AddTweetForm(request.POST)
        if form.is_valid():
            nickname = form.cleaned_data["nickname_input"]
            tweet = form.cleaned_data["tweet_input"]
            new_tweet = models.Tweet(nickname=nickname, tweet=tweet)
            new_tweet.save()
            return redirect(reverse("tweetapp:listtweet"))
        else:
            return render(request, "tweetapp/addtweetbyform.html", context={"form": form})
    else:
        form = forms.AddTweetForm()
        return render(request, "tweetapp/addtweetbyform.html", context={"form": form})
    
def addtweetbymodelform(request):
    if request.method == "POST":
        form = forms.AddTweetModelForm(request.POST)
        if form.is_valid():
            nickname = form.cleaned_data["nickname"]
            tweet = form.cleaned_data["tweet"]
            new_tweet = models.Tweet(nickname=nickname, tweet=tweet)
            new_tweet.save()
            return redirect(reverse("tweetapp:listtweet"))
        else:
            return render(request, "tweetapp/addtweetbymodelform.html", context={"form": form})
    else:
        form = forms.AddTweetModelForm()
        return render(request, "tweetapp/addtweetbymodelform.html", context={"form": form})
    
@login_required
def deletetweet(request, id):
    tweet = models.Tweet.objects.get(pk=id)
    if request.user == tweet.username:
        models.Tweet.objects.filter(id=id).delete()
        return redirect('tweetapp:listtweet')
class SignUpView(CreateView):
    form_class = UserCreationForm

    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"