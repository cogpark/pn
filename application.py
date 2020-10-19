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

    metadata = {"description": "We clarify information about voting in United States elections: Registration deadlines, how to vote early & absentee, and links to your state's critical information about voting.","title": "Voting information for all U.S. states"}   
    return render_template('voting-info.html', us_states=us_states, metadata=metadata)

@application.route('/attorney-general')
def attorney_general():
    metadata = {'description': "The attorney general is part of the president's cabinet and oversees the Department of Justice.", "title":"What are attorneys general and what do they do?"}

    return render_template('attorney-general.html', metadata=metadata)

@application.route('/all-elections')
def all_elections():
    metadata = {'description': "There are a lot of elections in U.S. politics--primaries and generals and midterms and specials and more", "title":"What are all the elections & what are they for?"}
    return render_template('all-elections.html', metadata=metadata)

@application.route('/amendments-eleven-through-twenty-seven')
def more_amendments():
    metadata = {'description': "What Amendments 11 through 27 say: Changes to the courts, electoral college, and civil rights.", "title":"Amendments 11 through 27"}
    return render_template('more-amendments.html', metadata=metadata)

@application.route('/bill-of-rights')
def bill_of_rights():
    metadata = {'description': "The Bill of Rights is the first 10 amendments to the Constitution. It was written by James Madison and ratified in 1791, 3 years after the Constitution was.", "title":"The Bill of Rights"}
    return render_template('bill-of-rights.html', metadata=metadata)

@application.route('/whats-a-conservative')
def conservative():
    metadata = {"description": "Conservatives believe Christian values should shape society and that government should be limited.", "title": "What is a conservative?"}
    return render_template('conservative.html', metadata=metadata)

@application.route('/whats-a-democrat')
def democrat():
    metadata = {"description":"Democrats think government should solve social problems and shouldn't regulate sexuality or individual identity.", "title":"What is a Democrat?"}
    return render_template('democrat.html', metadata=metadata)

@application.route('/democratic-socialist')
def democratic_socialist():
    metadata = {"description":"Democratic Socialists think government should serve the public good and they want to get rid capitalism.", "title":"What is a Democratic Socialist?"}
    return render_template('democratic-socialist.html', metadata=metadata)

@application.route('/electoral-college')
def electoral_college():
    metadata = {"description": "The electoral college is an indirect voting system. Voters vote for electors who then vote for president. There are 538 electors.", "title":"The electoral college"}
    return render_template('electoral-college.html', metadata=metadata)

@application.route('/executive-order')
def executive_order():
    return render_template('executive-orders.html')

@application.route('/house-of-representatives')
def house_of_reps():
    return render_template('house-of-representatives.html')

@application.route('/just-moved-voting')
def just_moved():
    return render_template('just-moved-voting.html')

@application.route('/left-right-political-spectrum')
def political_spectrum():
    return render_template('left-right-political-spectrum.html')

@application.route('/whats-a-liberal')
def liberal():
    return render_template('liberal.html')

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
