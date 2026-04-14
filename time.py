#imports
from flask import Flask
from datetime import datetime

app = Flask(__name__)
now = datetime.now()

#function
@app.route("/")    #F(X) decorator
def gittime():
    time = f"{now.strftime('%H:%M:%S')}<br/>{now}"
    return time

#mainloop
app.run(debug=True,host="0.0.0.0",port=3000)