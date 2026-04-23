#imports
from flask import Flask, request, redirect, url_for, Blueprint, jsonify
from routes import States

#var or object or global things
app = Flask(__name__)
app.register_blueprint(States.state_bp, url_prefix='/states')


#function
@app.route("/")    #F(X) decorator _> extra processing to the f(x)
def hello():
    #return "up and running"
    return redirect(url_for('welcome'))

@app.route("/welcome")
def welcome():
    out='''
    <head>
    <style>
        body {
            background-color: #3A3A3A;
            color: #FFF;
        }
        a{
            text-decoration:none;
        }
        a:link {
            color: #1E90FF;
        }
        a:visited {
            color: #b478ed;
        }
        a:hover {
            color: LightBlue;
        }
        a:active {
            color: purple;
        }
    </style>
    </head>
    <body>
    <h1>Welcome to the IoT API!</h1>
    <h2>This is a testing ground for the sictcweb API Flask Version</h2>
    Here are some routes you can use
    <ul>
    <li><a href="/states/welcome">GET /states/welcome</a></li>
    <li><a href="/states/">GET /states/</a></li>
    <li><a href="/states/id/1">GET /states/id/<id></a></li>
    <li>POST /states/add json</li>
    <li>DELETE /states/delete json</li>
    <li>GET /states/update json</li>
    </ul>
    </body>
    '''
    return out

#mainloop
app.run(debug=True,host="0.0.0.0",port=3000)