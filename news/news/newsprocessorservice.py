
import boto.sqs
from boto.sqs.message import Message

sqsconn = boto.sqs.connect_to_region("us-west-2",
aws_access_key_id = 'AKIAITXWEVDOIW3YSCGQ',
aws_secret_access_key = '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')

news_queue = sqsconn.get_queue('newsqueue')


def GetMessageFromQueue():
    # grab fisrt message from queue
    rs = news_queue.get_messages(message_attributes=['link','title', 'description')
    m = rs[0]

    raw_text = m.get_body()
    attr = m.message_attributes['link']['string_value']
#more elegant way to iterate through all of the message attibutes?
    return #some kind of object with story elements?

def NameTagService(story_object):
    #send raw text to name tagging service and append result to story object

def OtherService(story_object):
#repeat same as above for any other service as needed


def SendToNewsCRUD(story_object):
    #send resulting text to newsCRUD API to write to db
    
SendToNewsCRUD(NameTagService(GetMessageFromQueue))
