from flask import Flask, request, redirect, url_for, jsonify, Blueprint
import pymysql
#import os
#from dotenv import load_dotenv
from .DBConnections import connectToDB

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
    #print(queryString) #debug purposes
    #print(dbc)
    try:
        with dbc.cursor() as cursor:
            cursor.execute(queryString)
            rows = cursor.fetchall()
            print(type(rows))
            print(rows)
            #we could inject the rows into some html code to create table
            return str(rows), 200
    except pymysql.Error as e:
        return f"Pymysql error: {e}"
    except:
        return "oops something went wrong"
    return "get all"
