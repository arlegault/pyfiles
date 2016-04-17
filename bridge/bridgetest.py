
from flask import Flask, json, Response, render_template, request, redirect
import requests
import urllib2
import csv
app = Flask(__name__)
app.config['DEBUG'] = True

#readfromCSV('context_one.csv','action_mapping1')
#context_action_mapping={1:action_mapping1}

#def readfromCSV(csvname, dictname):
#    with open(csvname, 'rb') as infile:
#        reader = csv.reader(infile, delimiter = ',')
#        dictname = dict((rows[0],rows[1]) for rows in reader)#{rows[0]:rows[1] for rows in reader}
#        return dictname

#context_action_mapping=[readfromCSV('/home/ubuntu/alexaApp/context_one.csv','action_mapping1')]
#context_action_mapping={1:action_mapping1}
context_action_mapping = []

action_list_1 = {"circle":"can you repeat that","swipe":"no thank you I dont want that","screenTap":"I want that one right there","one":"one","two":"two","three":"three","four":"four","five":"five","six":"six","seven":"seven","eight":"eight ","nine":"nine","ten":"ten fuck yes I can count","pinch":"just a little bit","grab":"can I have the check please","fingerWake":"can you please help me",}

context_action_mapping.append(action_list_1)

@app.route('/translate/<text_to_translate>')
def translate(text_to_translate):
        payload = {'key': 'AIzaSyA_Pn91Io-unbYS5cAPkkoCjDigdwxcw1o', 'q': str(text_to_translate)}
            r = requests.get('https://www.googleapis.com/language/translate/v2/detect', params=payload)
                language_detected = r.json()['data']['detections'][0][0]['language']
payload = {'key': 'AIzaSyA_Pn91Io-unbYS5cAPkkoCjDigdwxcw1o', 'q': str(text_to_translate), 'source': str(language_detected), 'target': 'en'}

    t = requests.get('https://www.googleapis.com/language/translate/v2', params=payload)

        text_to_speak = t.json()['data']['translations'][0]['translatedText']
            return redirect('http://ec2-52-35-142-102.us-west-2.compute.amazonaws.com:9999/api/speech?textToSpeech=' + text_to_speak.encode('utf8')) #change this

@app.route('/')
def hello_world():
    return render_template('hello.html')

            #@app.route('/update/<key>/<pair>')
            #def udpateGestureList(key, pair):
            #    action_mapping[key] = pair
            #    return action_mapping.json()
@app.route('/leap/<action>', defaults={'context': 0})
@app.route('/leap/<action>/<context>')
def leapListner(action, context):

                    #Lookup which text we are supposed to return
                        text = context_action_mapping[context][str(action)]

                          # text = action_mapping.get(action)

                              #build payload and url request
                                  payload = {'textToSpeech': text.encode('utf8')}
                                   l = requests.get('http://ec2-52-35-142-102.us-west-2.compute.amazonaws.com:9999/api/speech', params=payload)
                                       return Response(l.content, mimetype='audio/mp3')


                                   #content type must be audio mp3 or whatever he sends me

                                   #establish alexa session?

                                   #process text

                                   #send to alexa


                                   if __name__ == '__main__':
                                           app.run(debug=True)

