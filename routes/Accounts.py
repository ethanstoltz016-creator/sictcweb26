from flask import Flask, request, redirect, url_for, jsonify, Blueprint
import pymysql
#import os
#from dotenv import load_dotenv
from .DBConnections import connectToDB

# global var and obj
account_bp = Blueprint('account_bp', __name__)
dbc = connectToDB()

#functions
@account_bp.route("/welcome")
def welcome():
    return "Hello and welcome to the Accounts route"

#GET/READ every record from Accounts Table
@account_bp.route('/')
def getAll():
    queryString = f"SELECT * FROM Accounts"   #!!! NOTICE NO ;
    #print(queryString) #debug purposes
    #print(dbc)
    try:
        with dbc.cursor() as cursor:
            cursor.execute(queryString)
            rows = cursor.fetchall()
            print(type(rows))
            print(rows)
            #we could inject the rows into some html code to create table
            
            return generate_account_table(rows), 200
    except pymysql.Error as e:
        return f"Pymysql error: {e}"
    except:
        return "oops something went wrong"

@account_bp.route('/id/<int:id>')     #<id> this is now a variable that the f(x) can run and get from the url
def getByID(id):
    queryString = f"SELECT * FROM Accounts WHERE Id={id}"
    try:
        with dbc.cursor() as cursor:
            cursor.execute(queryString)
            rows = cursor.fetchone()
            print(rows)
            userJsonData = []
            data={
                'id': rows[0],
                'Name': rows[1],
                'Address': rows[2],
                'City': rows[3],
                'State': rows[4],
                'Zip': rows[5]
            }
            userJsonData.append(data)
            
            return data,200
    except pymysql.Error as e:
        return f"Pymysql error: {e}"
    except Exception as e:
        return f"oops something went wrong"

#Add a state to the table
@account_bp.route('/add', methods=['POST'])   #Hey Flask, you're going to get a json object
def addIt():
    if request.is_json:
        data = request.get_json()           #request is a Flask module
        account = data.get('state')           #"State" cuz the keyword in json
    else:
        account = "OH"
    queryString = f"INSERT INTO Accounts (Account) VALUES ({account})"
    try:
        with dbc.cursor() as cursor:
            cursor.execute(queryString)
            dbc.commit()
            return "finished"
    except pymysql.Error as e:
        return f"Error connecting to db: {e}"


#Update a state in the table
@account_bp.route('/update/<int:id>', methods=['PUT'])   #Hey Flask, you're going to get a json object
def updateIt(id):
    if request.is_json:
        data = request.get_json()           #request is a Flask module
        id = data.get('Id')                 # Get the ID from the JSON data
        state = data.get('state')           #"State" cuz the keyword in json
    else:
        id = 1
        state = "OH"
    queryString = f"UPDATE Accounts SET Account = {state} WHERE Id = {id}"
    print(queryString)
    try:
        with dbc.cursor() as cursor:
            cursor.execute(queryString)
            dbc.commit()            #saves the request to the db
            return "finished"
    except pymysql.Error as e:
        return f"Error connecting to db: {e}"

#Delete a state in the table
@account_bp.route('/delete/<int:id>', methods=['DELETE'])   #Hey Flask, you're going to get a json object
def deleteIt(id):
    if request.is_json:
        data = request.get_json()
        id = data.get('Id')
    else:
        id = 1
    queryString = f"DELETE * FROM States WHERE Id = {id}"
    print(queryString)
    try:
        with dbc.cursor() as cursor:
            cursor.execute(queryString)
            dbc.commit()            #saves the request to the db
            return "finished"
    except pymysql.Error as e:
        return f"Error connecting to db: {e}"


def generate_account_table(data):
    """
    Converts a tuple of US states into a professional HTML table.
    Data format: ((1, 'IN'), (2, 'KY'), (3, 'IL'))
    """
    # Inline CSS to make the table look "pretty" without external files
    css = """
    <style>
        .state-table {
            width: 100%;
            max-width: 500px;
            border-collapse: collapse;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 20px auto;
            border: 1px solid #dee2e6;
        }
        .state-table thead {
            background-color: #004085;
            color: white;
        }
        .state-table th, .state-table td {
            padding: 12px 15px;
            text-align: left;
            border-bottom: 1px solid #dee2e6;
        }
        .state-table tbody tr:nth-child(even) {
            background-color: #f8f9fa;
        }
        .state-table tbody tr:hover {
            background-color: #e9ecef;
        }
        .header-text {
            text-align: center;
            color: #333;
            font-family: sans-serif;
        }
    </style>
    """

    # Start building the HTML string
    html = f"{css}<h2 class='header-text'>Account Registry</h2>"
    html += "<table class='state-table'><thead><tr><th>ID</th><th>Account/th></tr></thead><tbody>"

    # Iterate through the tuple of tuples
    for account_id, account_name in data:
        html += f"<tr><td>{account_id}</td><td><strong>{account_name}</strong></td></tr>"

    # Close the table
    html += "</tbody></table>"
    
    return html