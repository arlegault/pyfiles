from flask import Flask
from flask import request

app = Flask(__name__)

def writeToDb(feedback_dict):
    #TODO write info to db and return successful message
    return True

def processResponse(feedback_text):
    #TODO need to define what meta data we would like to extract/process from text and write to db. Should return a dict with the raw text and all meta data appended.
    return True


@app.route('/feedback/<text>', methods=['POST'])
def submitFeedback():
    processResponse()#figureout how to parse json from POST req
    return "Your feedback has been submitted"+ text


if __name__ == '__main__':
    app.run(debug=True)
