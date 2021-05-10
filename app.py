import cv2
import model
import os

import werkzeug
from flask import Flask, render_template, jsonify, request

from App.run_advise.advisor import Advisor

app = Flask(__name__)
UPLOAD_FOLDER = 'static'

@app.route("/")
def index():
    return render_template("index.html")

# Routing to all html templates
@app.route('/<string:htmltemp>')
def router(htmltemp):
    return render_template(htmltemp)

@app.route('/advise', methods = ['GET', 'POST'])
def advise():
   if request.method == 'POST':

      try:
          file = request.files['file']
          advisor = Advisor()
          advisor.learn(xes_file=file)
          result = advisor.think()
      except:
          result = "unsupported file"

      return result

@app.route("/results", methods=['GET', 'POST'])
def results():
    if request.method == 'POST':
        upload_file = request.files['file']
        filename = werkzeug.utils.secure_filename(upload_file.filename)
        my_path = os.path.abspath(os.path.dirname(__file__))
        upload_file.save(os.path.join(my_path, UPLOAD_FOLDER, filename))
        image = cv2.imread(os.path.join(my_path, UPLOAD_FOLDER, filename))

        return jsonify(model.predict(app.graph,image))

    return "Error"


my_path = os.path.abspath(os.path.dirname(__file__))
path = os.path.join(my_path, "static/model.pb")
app.graph = model.load_graph(path)

def runCamargo():
    camargo = Camargo()
    camargo.run()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=False)

