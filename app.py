from implementations.Camargo.camargo import Camargo

from flask import Flask, render_template, jsonify, request
import werkzeug
import base64, os, model, cv2

app = Flask(__name__)
UPLOAD_FOLDER = 'static'

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/results",methods=['GET','POST'])
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
    app.run(host="0.0.0.0",port=5000,debug=True,use_reloader=False)

