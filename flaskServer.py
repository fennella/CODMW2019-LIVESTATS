from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import requests
import json
import random

app = Flask(__name__)
CORS(app)
port = '5000'

@app.route('/', methods=['GET'])
def index():

    return render_template('index.html')

@app.route('/getStats', methods=['GET'])
def getStats():
    
    response = requests.get("https://api.dreamteam.gg/games/cod/players/xbl/import%20winner/stats")
    jsonData = json.loads(response.text)

    statsDict = {}

    kdSpread = jsonData['lifetime']['all']['kd_ratio']
    scorePerMinute = jsonData['lifetime']['all']['score_per_minute']
    scorePerGame = jsonData['lifetime']['all']['score_per_game']
    wlRatio = jsonData['lifetime']['all']['wl_ratio']
    longestStreak = jsonData['lifetime']['all']['longest_streak']
    killsPerGame = jsonData['lifetime']['all']['kills'] / jsonData['lifetime']['all']['matches_played']
    killsPerMinute = jsonData['lifetime']['all']['kills'] / (jsonData['lifetime']['all']['time_played'] / 60)
    accuracy = jsonData['lifetime']['all']['accuracy']


    statsDict['kdSpread'] = kdSpread
    #statsDict['kdSpread'] = random.uniform(0, 1)
    statsDict['scorePerMinute'] = scorePerMinute
    statsDict['scorePerGame'] = scorePerGame
    statsDict['wlRatio'] = wlRatio
    statsDict['longestStreak'] = longestStreak
    statsDict['killsPerGame'] = killsPerGame
    statsDict['killsPerMinute'] = killsPerMinute
    statsDict['accuracy'] = accuracy

    return jsonify(statsDict)

app.run(port=port)

