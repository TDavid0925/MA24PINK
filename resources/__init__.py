from flask import Flask
from flaskext.mysql import MySQL

application = Flask(__name__)

"""
Connecting to the DB
"""
application.config['MYSQL_DATABASE_HOST'] = 'ma24.ccvsxtfllqzc.us-east-2.rds.amazonaws.com'
application.config['MYSQL_DATABASE_PORT'] = 3306
application.config['MYSQL_DATABASE_USER'] = "David"
application.config['MYSQL_DATABASE_PASSWORD'] = "MA24Pink"
application.config['MYSQL_DATABASE_DB'] = 'Pink'
mysql = MySQL(application)
