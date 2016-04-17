import csv
import random
from flask import Flask
from flask import request

app = Flask(__name__)

def readCSVtoList(csvname, arrayname):
    with open(csvname, 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter = ',')
        for row in reader:
            arrayname.append(row)

@app.route('/jokes', methods=['GET'])
def JdJokes():
    if not request.json:

        joke_array = []
        readCSVtoList('jeffdeanjokes.csv', joke_array)

        return random.choice(joke_array)[0]
    else:
        return "not json"



@app.route('/advice', methods=['GET'])
def JeffAdvice():

    advice_array = []
    readCSVtoList('jeffdeanadvice.csv', advice_array)

    return random.choice(advice_array)[0]



@app.route('/numbers', methods=['GET'])
def numbersEveryEngineerShouldKnow():

    numbers_array = []
    readCSVtoList('importantnumbers.csv', numbers_array)

    return random.choice(numbers_array)[0]



if __name__ == '__main__':
    app.run(debug=True)
