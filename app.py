from flask import Flask, request, jsonify
from flask_cors import CORS
import json, requests

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
  return 'Proxy api'

locations = {
  "Rittenhouse Square": {
    '8/11': {
      'Caitlyn Bot': '8:00',
      'Ahri Bot': '9:00',
      'Diana Bot': '15:00'
    },
    '8/12': {
      'Thresh Bot': '8:00',
    },
    '8/13': {
      'Taric Bot': '13:00',
      'Graves Bot': '15:00'
    }
  },
  "Drexel Park": {
    '8/11': {
      'Kalista Bot': '7:00',
      'Ahri Bot': '11:00'
    },
    '8/12': {
      'Teemo Bot': '18:00',
      'Yone Bot': '20:00',
      'Camille Bot': '23:00'
    },
    '8/13': {
      'Yuumi Bot': '13:00',
      'Syndra Bot': '15:00'
    }
  },
  "34th Station": {
    '8/11': {
      'Amumu Bot': '8:00',
      'Ashe Bot': '11:00',
      'Azir Bot': '15:00'
    },
    '8/12': {
      'Trundle Bot': '11:00',
      'Yasuo Bot': '20:00'
    },
    '8/13': {
      'Yuumi Bot': '13:00',
      'Syndra Bot': '15:00'
    }
  },
  "Mario Statue": {
    '8/11': {
      'Draven Bot': '6:00',
      'Lucian Bot': '12:00',
      'Annie Bot': '13:00'
    },
    '8/12': {
      'Senna Bot': '17:00',
      'Sivir Bot': '22:00'
    },
    '8/13': {
      'Jax Bot': '17:00',
      'Darius Bot': '22:00',
      'Akali Bot': '23:00'
    }
  }
}

@app.route('/api_get', methods=['GET'])
def api_get():
  return jsonify(locations)

@app.route('/api_post', methods=['POST'])
def api_post():
  # deserializing
  data = request.data
  data = json.loads(data)
  print("POST data received:", data)
  print(data["location"])
  locations[data["location"]][data["date"]][data["name"]] = data["time"]
  return 'OK'


if __name__=='__main__':
  app.run(debug=True)