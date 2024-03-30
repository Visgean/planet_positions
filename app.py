from flask import Flask, jsonify
from skyfield.api import load

planets = load('de421.bsp')

selection = {
    'earth',
    'mars',
    'moon',
    'SATURN BARYCENTER',
    'URANUS BARYCENTER',
    'PLUTO BARYCENTER',
    'jupiter BARYCENTER',
    'mercury',
    'neptune BARYCENTER',
    'sun',
    'venus BARYCENTER',
}

app = Flask(__name__)

@app.route("/")
def planet_positions():
    ts = load.timescale()
    t = ts.now()

    result = {}
    for p in selection:
        planet_name = p.split(' ')[0].lower()
        result[planet_name] = list(planets[p].at(t).position.au)

    response = jsonify(result)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
