from flask import Flask, render_template, request
from flask_restful import Api

from resources.charities import CharityList
from resources.emergencies import EmergencyList
from resources.hospitals import HospitalList 


"""
Make an application instance
"""
application = Flask(__name__)
api=Api(application)

"""
API register
"""
api.add_resource(CharityList, '/api/charities/<string:location>')
api.add_resource(EmergencyList, '/api/emergencies/<string:location>')
api.add_resource(HospitalList, '/api/hospitals/<string:location>')


"""
route configuration is here
"""
@application.route('/')
@application.route('/index')
def index():
    return render_template('index.html')

@application.route('/dom_vio_sta')
@application.route('/index/dom_vio_sta')
def dom_vio_sta():
    return render_template('dom_vio_sta.html')

@application.route('/social_help')
@application.route('/index/social_help')
def social_help():
    return render_template("social_help.html")

if __name__ == '__main__':
    application.debug = True
    application.run()