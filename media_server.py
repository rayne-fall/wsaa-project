from flask import Flask, jsonify
#https://www.geeksforgeeks.org/websites-apps/cross-origin-resource-sharing-cors/
from flask_cors import CORS, cross_origin
from DAO import mediaDAO

app = Flask(__name__)
cors = CORS(app) # allow cross-origin resource sharing

app = Flask(__name__, static_url_path='', static_folder='.')

# 127.0.0.1:5000/
@app.route('/')
@cross_origin()
def index():
    return 'Hello World!'

# 127.0.0.1:5000/tvshows
@app.route('/tvshows')
@cross_origin()
def getAlltvShows():
    results=mediaDAO().getAlltv()
    return jsonify(results)

# 127.0.0.1:5000//<int:id>
@app.route('/tvshows/<int:id>')
@cross_origin()
def findTVById(id):
    foundTV = mediaDAO().findTVByID(id)

    return jsonify(foundTV)

# run the server with the debugger
if __name__=='__main__':
    app.run(debug=True)