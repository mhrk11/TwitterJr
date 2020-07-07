from django.urls import path
from .views import HomePageView, CreateTweet, TweetDetail, TweetUpdate, TweetDelete


urlpatterns=[
    path('', HomePageView.as_view(), name='home'),
    path('tweet/new/', CreateTweet.as_view(), name='new_tweet'),
    path('tweet/<int:pk>/', TweetDetail.as_view(), name='tweet_detail'),
    path('tweet/<int:pk>/edit/', TweetUpdate.as_view(), name='tweet_update'),
    path('tweet/<int:pk>/delete/', TweetDelete.as_view(), name='tweet_delete'),



    ]
