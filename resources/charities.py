from flask import Flask, Blueprint
from flask_restful import Resource

charityList = [
    {
        "name": "HousingFirst Ltd",
        "Services": ["Victims_of_crim", "Poeple_at_risk_of_homelessness"],
        "LGA": "Melbourne"
    },
    {
        "name": "Pink Cross Foundation Australia",
        "Services": ["Victims_of_crim", "Poeple_at_risk_of_homelessness"],
        "LGA": "South Melbourne"
    }
]

class CharityList(Resource):
    def get(self, location):
        if (location==""):
            return charityList
        else:
            return charityList