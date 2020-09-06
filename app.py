from flask import Flask, render_template
import os
import json
from static.data.absentee_voting import absentee_data
from static.data.covid import covid_data
from static.data.id_requirements import id_data
from static.data.reg_deadlines_2020 import reg_data

app = Flask(__name__)


@app.route("/")
def index():
    us_states = ['Alabama','Alaska', 'Arizona','Arkansas','California',
        'Colorado','Connecticut','Delaware',
        'Florida','Georgia','Hawaii',
        'Idaho','Illinois','Indiana','Iowa','Kansas','Kentucky',
        'Louisiana','Maryland','Massachusetts','Michigan','Minnesota','Mississippi','Missouri',
        'Montana','Nebraska','Nevada','New Hampshire','New Jersey',
        'New Mexico','New York','North Carolina','North Dakota',
        'Ohio','Oklahoma','Oregon', 'Pennsylvania','Rhode Island','South Carolina',
        'South Dakota','Tennessee','Texas','Utah','Vermont',
        'Virginia','Washington', 'Washington, D.C.',
        'West Virginia','Wisconsin',
        'Wyoming']
    print(us_states)
    
    return render_template('voting-info.html', us_states=us_states)

@app.route("/all-elections")
def all_elections():
    return render_template('all-elections.html')


@app.route('/api/absentee/<state>')
def send_absentee_data(state):
    return json.dumps(absentee_data[state])

@app.route('/api/id/<state>')
def send_id_data(state):
    return json.dumps(id_data[state])

@app.route('/api/registration/<election>/<state>')
def send_reg_data(election, state):
    return json.dumps(reg_data[election][state])

@app.route('/api/covid/<state>')
def send_covid_data(state):
    return json.dumps(covid_data[state])

if __name__ == "__main__":
    app.run(debug=True)
