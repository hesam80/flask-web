from flask import Flask
import time

app = FLASK(__name__)

@app.route('/api/time')
def get_current_time():
    return {'time': time.time()}

if __name__ == '__main__':
    app.run(debug=True)