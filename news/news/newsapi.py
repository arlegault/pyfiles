#news settings. this will be an API to interface with to front end setup (feeds and settings). THis will also inform the news processor module on what to do as well.

import sqlite3
from flask import Flask
from flask import request
import json

app = Flask(__name__) #setup flask


@app.route('/sources', methods=['POST'])
def AddNewsSource(source_link):
    #TODO verify does not already exist in news db
    #TODO verify the source is valid
    #TODO get source info. Name, formatting, favicon?, etc
    #TODO add source and xtra info to database
    return True


@app.route('/sources', methods=['GET'])
def GetNewsSources():

    dbconn=sqlite3.connect('/home/alex/pyfiles/news/news/news.sqlite')
    db = dbconn.cursor()
    sources = db.execute('SELECT name, rss_link FROM news_sources')

    list_of_feeds = []
    for i in sources:
        list_of_feeds.append(i)

    dbconn.close()

    return json.dumps(list_of_feeds) 


@app.route('/recent/<source>', methods=['GET'])
def GetMostRecentStory(source):
    dbconn=sqlite3.connect('/home/alex/pyfiles/news/news/news.sqlite')
    db = dbconn.cursor()
    most_recent =  db.execute('SELECT link, MAX(pubdate) FROM news_stories WHERE source =     ? GROUP BY link, source',(source,))
    resp = []
    for i in most_recent:
        resp.append(i)

    dbconn.close()

    return json.dumps(resp)


@app.route('/sources/<source_name>', methods= ['DELETE'])
def RemoveNewsSource(source_name):
    dbconn=sqlite3.connect('/home/alex/pyfiles/news/news/news.sqlite')
    db = dbconn.cursor()
    db.execute('DELETE from news_sources WHERE name = ?', (source_name,))
    dbconn.commit()
    dbconn.close()
    return 'success' #should add a validation that delete occured else return error to user


@app.route('/sources', methods=['PUT'])
def ChangeNewsSource(link, source_name):#need to look at how many args needed
    dbconn=sqlite3.connect('/home/alex/pyfiles/news/news/news.sqlite')
    db = dbconn.cursor()
    db.execute('UPDATE news_sources SET rss_link = ? WHERE name = ?', (link, source_name,))
    dbconn.commit()
    dbconn.close()
    return 'success' #should add a validation b4 returning success

@app.route('/write', methods=['POST'])
def WriteStory(link, title, source, pubdate, desc, text):
    dbconn=sqlite3.connect('/home/alex/pyfiles/news/news/news.sqlite')
    db = dbconn.cursor()
    db.execute('INSERT INTO news_stories VALUES (?,?,?,?,?,?)', (link, title, source, pubdate, desc, text,))
    dbconn.close()

    return 'success'

if __name__ == '__main__':
    app.run(debug=True)
