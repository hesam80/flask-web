from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def view():
    return 'Congratulations, you successfully deployed a container image to Cloud Run!'
   

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)