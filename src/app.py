#!/usr/bin/env python3
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, render_template
import requests
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, JSON

#,"team":"38"}

url = "https://api-football-v1.p.rapidapi.com/v3/teams/statistics"

#querystring = {"league":"39","season":"2020","team":"40"}

headers = {
	"X-RapidAPI-Key": "2735a11d4fmsh2567ef89483ead0p197923jsn09bf45131248",
	"X-RapidAPI-Host": "api-football-v1.p.rapidapi.com"
}

#engine = create_engine("postgresql://teamstats:teamstats@127.0.0.1:5432/")

#Session = sessionmaker(engine)




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://teamstats:teamstats@127.0.0.1:5432/teamstats'

db = SQLAlchemy(app)

engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
metadata_obj = MetaData()

if not database_exists(app.config['SQLALCHEMY_DATABASE_URI']):
    create_database(app.config['SQLALCHEMY_DATABASE_URI'])
try:
    teamstats = Table(
        'teamstats',
        metadata_obj,
        Column('teamid', Integer, primary_key=True),
        Column('teamname', String),
    )
    teamstats.create(engine)
except: 
    pass

class Teamstats(db.Model):
    teamid = db.Column(db.Integer, primary_key=True)
    teamname = db.Column(db.String, nullable=True)
    
#gamesplayed = db.Column(db.Integer, nullable=True)
#gameswon = db.Column(db.Integer, nullable=True)
    

        

#def get_teamname():
#    response = requests.get(url, headers=headers, params=querystring)
#    return response.json()["team"][1]

#def get_teamname():
    #db.session.begin()
    #response = requests.get(url, headers=headers, params=querystring)
    #json.dumps(Teamstats)
    #new_entry = Teamstats(teamname=response.json()['response']['team']['name'])
    #db.session.add(new_entry)
    #db.session.commit()
        

    #return response.json()['response']['team']['name']

#,
#                           gamesplayed=response.json()['response']['Fixtures']['played']['total'],
#                           gameswon=response.json()['response']['Fixtures']['wins']['total'])

def get_name_and_id():
    #db.session.begin()
    input_text = request.form.get("user_input", "")
    querystring = {"league":"39","season":"2020","team":input_text}
    response = requests.get(url, headers=headers, params=querystring)
    #apiresponse = json.loads(str(response))
    new_entry = Teamstats(teamid=response.json()['response']['team']['id'], 
                           teamname=response.json()['response']['team']['name'])
    #jsonpickle.encode(new_entry)
    db.session.query(Teamstats).delete()
    db.session.commit()
    db.session.add(new_entry)
    db.session.commit()
        
    #return response.json()['response']['team']['id']

@app.route("/")
def main():
    return '''
     <form action="/api_output" method="POST">
         <text> Enter a team number 1-40 </text>
         <input name="user_input">
         <input type="submit" value="Show Team Stats">
     </form>
     
     '''

@app.route("/echo_user_input", methods=["POST"])
def echo_input():
    input_text = request.form.get("user_input", "")
    return "You entered: " + input_text

@app.route("/api_output", methods=["POST"])
def index():
    #get_name_and_id()
    #team_stats = Teamstats.query.all()
    #return team_stats
    try:
        get_name_and_id()
        teamstats_all = Teamstats.query.all()

        #teamstats_text = '<ul>'

        #for team in teamstats_all:
        #    teamstats_text += '<li>' + team.teamname + ', ' + str(team.teamid) + '</li>'
        #teamstats_text += '</ul>'
        return render_template('index.html', teamstats=teamstats_all)
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text


#def getteamnameandid():
#    get_teamname()
#    get_teamid()


#def get_teamname():
#    response = requests.get(url, headers=headers, params=querystring)
#    return response.json()['response']['team']['name']
#def get_teamid():
#    response = requests.get(url, headers=headers, params=querystring)
#    return response.json()['response']['team']['id']

#def echo_api_output():
#    return (data.decode("utf-8"))

#if __name__ == "__main__":
#    with Session(engine) as session:
#        session.add()
#    team_name = get_teamname()
#    team_id = get_teamid()
#    new_entry = Teamstats(teamname=team_name)
#    new_entry2 = Teamstats(teamid=team_id)
#    db.session.add(new_entry)
#    db.session.add(new_entry2)
#    db.session.commit()
#    db.session.query(Teamstats)
