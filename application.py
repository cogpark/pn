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

    metadata = {"description": "We clarify information about voting in United States elections: Registration deadlines, how to vote early & absentee, and links to your state's critical information about voting.","title": "Voting information for all U.S. states", "keywords":"voter registration, registration deadlines, voter ID, voter ID requirements, vote by mail"}   
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

@application.route('/constitution-united-states')
def constitution():
    metadata = {"description": "The Constitution was written in 1787 and ratified in 1788. It lays out a structure for our government.", "title": "The Constitution of the United States", "keywords":"constitution, U.S. government, founding document, constitution ratified"}
    return render_template('constitution.html', metadata=metadata)

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
    metadata = {"description": "An executive order is an official instruction that the President of the United States issues to a federal agency.", "title":"What is an executive order?"}
    return render_template('executive-orders.html', metadata=metadata)

@application.route('/house-of-representatives')
def house_of_reps():
    metadata = {"description":"The House of Representatives is a group of 435 elected political leaders who make and approve new laws. The House and Senate together make up the U.S. Congress.", "title":"The House of Representatives of the United States"}
    return render_template('house-of-representatives.html', metadata=metadata)

@application.route('/just-moved-voting')
def just_moved():
    metadata = {"description":"If you've just moved, here are the steps to take to figure out how to register and vote your new state.", "title":"How to register & vote if you just moved"}
    return render_template('just-moved-voting.html', metadata=metadata)

@application.route('/left-right-political-spectrum')
def political_spectrum():
    metadata = {"description": "Left-wing and right-wing are opposing political perspectives. Right-wing ideas are more conservativ and leftist ideas being more progressive or liberal.", "title": "What left and right mean in U.S. politics"}
    return render_template('left-right-political-spectrum.html', metadata=metadata)

@application.route('/whats-a-liberal')
def liberal():
    metadata = {"description":"Liberal means progressive, but also refers to long philosophical tradition that doesn’t always align with the Democratic party.", "title":"What does liberal mean (in U.S. politics)"}
    return render_template('liberal.html', metadata=metadata)

@application.route('/whats-a-liberatarian')
def libertarian():
    metadata = {"description":"The Libertarian party was formed in 1971 believes that government should have as small a role as possible in our lives", "title":"What's a Libertarian"}
    return render_template('libertarian.html', metadata=metadata)

@application.route('/whats-a-republican')
def republican():
    metadata = {"description":"The Replublican party, sometimes called the Grand Old Party or GOP, is 1 of the 2 major political parties in U.S. politics today.", "title":"What's a Republican"}
    return render_template('republican.html', metadata=metadata)

@application.route('/supreme-court')
def supreme_court():
    metadata = {"description":"The Supreme Court is the most authoritative court U.S. It consists of 9 Justices whose combined judgment is a key part of how our government works.", "title":"The Supreme Court of the United States"}
    return render_template('supreme-court.html', metadata=metadata)

@application.route('/the-us-senate')
def senate():
    metadata = {"description":"The Senate is 100 elected political leaders who make and approve new laws. The Senate and the House of Representatives make up the Congress.", "title":"The Senate of the United States"}
    return render_template('the-us-senate.html', metadata=metadata)

@application.route('/taxes')
def what_are_taxes():
    metadata = {"description":"Taxes are money you pay to your federa, state, and local governments. Governments then use this money to fund services.", "title":"What are taxes?"}
    return render_template('taxes.html', metadata=metadata)

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
