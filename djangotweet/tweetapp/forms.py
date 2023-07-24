from django import forms
from django.forms import ModelForm
from tweetapp.models import Tweet

class AddTweetForm(forms.Form):
    nickname_input = forms.CharField(label="username", max_length=50)
    tweet_input = forms.CharField(label="Tweet", max_length=100,
                                  widget=forms.Textarea(attrs={"class":"tweetmessage"}))
    

class AddTweetModelForm(ModelForm):
    class Meta:
        model = Tweet
        fields = ['username', 'tweet']