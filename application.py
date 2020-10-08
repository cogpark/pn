from flask import Flask, render_template
import os
import json

application = Flask(__name__)


@application.route("/")
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
   
    return render_template('voting-info.html', us_states=us_states)

<<<<<<< HEAD
@application.route('/attorney-general')
def attorney_general():
    return render_template('attorney-general.html')

=======
>>>>>>> 00ee5232833c6b17a82e2617f8418a7cf4c1c8f3
@application.route('/all-elections')
def all_elections():
    return render_template('all-elections.html')

<<<<<<< HEAD
@application.route('/amendments-eleven-through-twenty-seven')
=======
@application.route('/amendments-eleven-through-twenty-six')
>>>>>>> 00ee5232833c6b17a82e2617f8418a7cf4c1c8f3
def more_amendments():
    return render_template('more-amendments.html')

@application.route('/bill-of-rights')
def bill_of_rights():
    return render_template('bill-of-rights.html')

@application.route('/whats-a-conservative')
def conservative():
    return render_template('conservative.html')

@application.route('/whats-a-democrat')
def democrat():
    return render_template('democrat.html')

@application.route('/democratic-socialist')
def democratic_socialist():
    return render_template('democratic-socialist.html')

@application.route('/electoral-college')
def electoral_college():
    return render_template('electoral-college.html')

@application.route('/executive-order')
def executive_order():
<<<<<<< HEAD
    return render_template('executive-orders.html')
=======
    return render_template('executive-order.html')
>>>>>>> 00ee5232833c6b17a82e2617f8418a7cf4c1c8f3

@application.route('/house-of-representatives')
def house_of_reps():
    return render_template('house-of-representatives.html')

@application.route('/just-moved-voting')
def just_moved():
    return render_template('just-moved-voting.html')

@application.route('/whats-a-liberal')
def liberal():
<<<<<<< HEAD
    return render_template('liberal.html')
=======
    return render_template('whats-a-liberal.html')
>>>>>>> 00ee5232833c6b17a82e2617f8418a7cf4c1c8f3

@application.route('/whats-a-liberatarian')
def libertarian():
    return render_template('libertarian.html')

@application.route('/whats-a-republican')
def republican():
    return render_template('republican.html')

@application.route('/supreme-court')
def supreme_court():
    return render_template('supreme-court.html')

@application.route('/the-us-senate')
def senate():
    return render_template('the-us-senate.html')

@application.route('/taxes')
def what_are_taxes():
    return render_template('taxes.html')

@application.route('/api/absentee/<state>')
def send_absentee_data(state):
    with open('static/data/absentee_data.json') as f:
        data = json.load(f)

    return json.dumps(data[state])

@application.route('/api/id/<state>')
def send_id_data(state):
    with open('static/data/id_data.json') as f:
        data = json.load(f)

    return json.dumps(data[state])

@application.route('/api/registration/<election>/<state>')
def send_reg_data(election, state):
    with open('static/data/reg_data_2020.json') as f:
        data = json.load(f)

    return json.dumps(data[election][state])

@application.route('/api/covid/<state>')
def send_covid_data(state):
    with open('static/data/covid_data.json') as f:
        data = json.load(f)

    return json.dumps(data[state]) 


@application.route('/sitemap')
def sitemap():
     return render_template('sitemap.xml')

if __name__ == "__main__":
    application.run()
