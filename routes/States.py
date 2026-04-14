from flask import Flask, request, redirect, url_for, jsonify, Blueprint
#import pymysql
#import os
#from dotenv import load_dotenv

# global var and obj
state_bp = Blueprint('state_bp', __name__)

#functions
@state_bp.route("/welcome")
def welcome():
    return "Hello and welcome to the States route"

#mainloop - not needed