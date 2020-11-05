#export FLASK_APP=hello.py
#export FLASK_ENV=development
#flask run

from flask import Flask
app = Flask(__name__)
@app.route('/')
def index():
    return "hoj"

if __name__ == "__main__":
    app.run(debug=True)



