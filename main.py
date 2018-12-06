from flask import Flask, render_template
from highlight import PiThing

app = Flask(__name__)
pi_thing = PiThing()


@app.route('/')
def main():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
