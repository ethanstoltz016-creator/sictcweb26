from flask import Flask, request, redirect, url_for, jsonify, Blueprint
#import pymysql
#import os
#from dotenv import load_dotenv
from sictcweb26.DBConnections import connectToDB

# global var and obj
state_bp = Blueprint('state_bp', __name__)
dbc = connectToDB()

#functions
@state_bp.route("/welcome")
def welcome():
    return "Hello and welcome to the States route"

#GET/READ every record from States Table
@state_bp.route('/')
def getAll():
    queryString = f"SELECT * FROM States"   #!!! NOTICE NO ;
    print(queryString) #debug purposes
    print(dbc)
    return "get all"
