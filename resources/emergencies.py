from flask_restful import Resource
from resources import mysql
#from models.models import test


class EmergencyList(Resource):
    
    def get(self, location):
        cur = mysql.connect().cursor()
        cur.execute('''SELECT * FROM test_table''')
        data = cur.fetchall()
        emergencyList = []
        for item in data:
            dic = {"id": item[0], "name": item[1], "location": item[2]}
            emergencyList.append(dic)
        
        #tests = test.query.all()
        #for t in tests:
        #    emergencyList.append(t)
        if (location==""):
            return emergencyList
        else:
            return emergencyList