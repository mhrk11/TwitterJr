from django.shortcuts import render
from .models import Tweet
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class HomePageView(ListView):
    model=Tweet
    template_name='home.html'
    context_object_name='tweets_list'
class CreateTweet(CreateView):
    model=Tweet
    template_name='new_tweet.html'
    fields=['title', 'author', 'body']
class TweetDetail(DetailView):
    model=Tweet
    template_name='tweet_detail.html'
class TweetUpdate(UpdateView):
    model=Tweet
    template_name='tweet_update.html'
    fields=['title', 'body']
class TweetDelete(DeleteView):
    model=Tweet
    template_name='tweet_delete.html'
    success_url=reverse_lazy('home')





# Create your views here.
