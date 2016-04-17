import feedparser
import boto3
#from boto.sqs.message import Message
from goose import Goose
import requests
import json

g = Goose()

#sqsconn = boto.sqs.connect_to_region("us-west-2",
#aws_access_key_id = 'redacted',
#aws_secret_access_key = 'redacted')
sqs = boto3.resource('sqs')
news_queue = sqs.get_queue_by_name(QueueName='newsqueue')
#news_queue = sqsconn.get_queue('newsqueue')

def GetFeeds():
    list_of_feeds = requests.get('http://127.0.0.1:5000/sources')
    if list_of_feeds.status_code != 200:
        raise ApiError('GET /sources {}'.format(list_of_feeds.status_code))
    
    # call the news setting API to get all feed links
    for i in list_of_feeds.json():
        CrawlFeeds(i)

def GetMostRecentStory(source):

    last_story = requests.get('http://127.0.0.1:5000/recent/'+ source)#need to pass source name or link to api so it can return something...
    if last_story.status_code != 200:
        raise ApiError('GET /recent {}'.format(list_of_feeds.status_code))

    return last_story.json()

def CrawlFeeds(feed_link):
    #TODO crawl stories
    feed = feedparser.parse(feed_link[1])
    latest_story = GetMostRecentStory(feed_link[0])

    for i in range(0, len(feed.entries)):
        title = feed.entries[i].title
        story_link = feed.entries[i].id
        description = feed.entries[i].description
       
        story_dict = dict(title=title, link=story_link, description=description)
#probably should parse more here

        if story_link != latest_story: #if story exists then dont process it
            ProcessStory(story_dict)
#put all this shit in a dict?

def ProcessStory(dict_with_story_attr):
 
    url = dict_with_story_attr['link']
    article = g.extract(url=url)

    dict_with_story_attr['cleantext'] = article.cleaned_text[:150]
    
    SendToQueue(dict_with_story_attr)

def SendToQueue(story_dict):
    
   # m = Message()
   # m.set_body(story_dict['cleantext'])
  #  m.message_attributes ={

    news_queue.send_message(
            MessageBody=story_dict['cleantext'],
            MessageAttributes={
                "link": {
                    "StringValue": story_dict['link'].encode("utf8"),
                    'DataType': 'String'},
                "title": {
                    "StringValue": story_dict['title'].encode("utf8"),
                    'DataType': 'String'},
                "description": {
                    "StringValue": story_dict['description'].encode("utf8"),
                    'DataType': 'String'} #how to encode weird shit in desc? typemustbe string but this returns a failure to encode errpr
}
    )

   # news_queue.write(m)

GetFeeds()
