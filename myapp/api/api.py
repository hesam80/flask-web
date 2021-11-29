import time
from flask import Flask

app = Flask(__name__)

@app.route('/api/time')
def get_current_time():
    return {'time': time.time()}

#Running and Controlling the script
if (__name__ =="__main__"):
 app.run(debug=True)