import base64
from os.path import basename

import matplotlib.pyplot as plt
import io
import base64

import cv2


import model
import os

import werkzeug
from flask import Flask, render_template, jsonify, request, current_app, send_from_directory

from App.run_advise.advisor import Advisor

app = Flask(__name__)
UPLOAD_FOLDER = 'static'
import zipfile
from flask import send_file
from flask import Flask,redirect

@app.route("/")
def index():
    return redirect(request.host_url + "menu")


@app.route("/menu")
def menu():
    return render_template("index.html")

# Routing to all html templates
@app.route('/<string:htmltemp>')
def router(htmltemp):
    return render_template(htmltemp)


@app.route('/advise', methods=['GET', 'POST'])
def advise():
   if request.method == 'POST':
      try:

          prediction = request.form.get('tvalue')
          file = request.files['file']
          advisor = Advisor()
          advisor.learn(xes_file=file)
          result = advisor.think(prediction=prediction)
      except:
          result = "unsupported file"

      return result

@app.route("/advisor_results", methods=['GET', 'POST'])
def advisor_results():
    if request.method == 'POST':
        upload_file = request.files['file']
        filename = werkzeug.utils.secure_filename(upload_file.filename)
        my_path = os.path.abspath(os.path.dirname(__file__))
        upload_file.save(os.path.join(my_path, UPLOAD_FOLDER, filename))
        image = cv2.imread(os.path.join(my_path, UPLOAD_FOLDER, filename))

        return jsonify(model.predict(app.graph,image))

    return "Error"


@app.route('/running/<string:type>', methods=['GET', 'POST'])
def running(type):
   app.config['DATA'] = request.form.get('data')
   app.config['METHOD'] = request.form.get('method')

   if request.method == 'POST':
       return render_template("running.html"), {"Refresh": "3; url="+request.host_url+type+"_result"}

@app.route('/train_result', methods=['GET', 'POST'])
def train_result():
    return render_template("train_result.html")

@app.route('/predict_result', methods=['GET', 'POST'])
def predict_result():

    return render_template("predict_result.html")

@app.route('/downloads/', methods=['GET', 'POST'])
def download():
    data = app.config['DATA']
    method = app.config['METHOD']

    filename = f"predictions/execution/output/{data}/models/{method}/"

    # current_appuploads = os.path.join(current_app.root_path, filename)
    # return send_from_directory(current_appuploads, as_attachment=True)
    zipf = zipfile.ZipFile('model.zip', 'w', zipfile.ZIP_DEFLATED)
    for root, dirs, files in os.walk(filename):
        for file in files:
            location = os.path.join(root, file)
            zipf.write(location, basename(location))
    zipf.close()

    return send_file('model.zip',
                     mimetype='zip',
                     attachment_filename='model.zip',
                     as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=False)

