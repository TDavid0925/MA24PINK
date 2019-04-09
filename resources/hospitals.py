from flask_restful import Resource

hospitalList = [
    {
        "name": "East Melbourne Specialist Day Hospital",
        "Type": "Private",
        "LGA": "Melbourne"
    },
    {
        "name": "Windsor Avenue Day Surgery",
        "Type": "Private",
        "LGA": "Greater Dandenong"
    }
]

class HospitalList(Resource):
    def get(self, location):
        if(location==""):
            return hospitalList
        else:
            return hospitalList
    