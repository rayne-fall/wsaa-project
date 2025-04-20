# project server
# auther: Sylvia Chapman Kent
# flask server 

from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello"

# debugging
if __name__ == "__main__":
    app.run(debug=True)

# viewing stored entries
@app.route('/games', methods=['GET'])
def getall():
    return "get all"

@app.route('/films', methods=['GET'])
def getall():
    return "get all"

# creating new entries
@app.route('/games', methods=['POST'])
def create():
    jsonstring=request.json
    return f"create {jsonstring}"

@app.route('/films', methods=['POST'])
def create():
    jsonstring=request.json
    return f"create {jsonstring}"