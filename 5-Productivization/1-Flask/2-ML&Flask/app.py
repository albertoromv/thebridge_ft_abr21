from flask import Flask, render_template, request
import pickle
import numpy as np
import os

os.chdir(r'C:\Users\Admin\Documents\GitHub\thebridge_ft_abr21\5-Productivization\1-Flask\2-ML&Flask')

model = pickle.load(open('iri.pkl', 'rb'))
app = Flask(__name__)

@app.route("/", methods = ["GET"])
def man():
    return render_template("home.html")

@app.route("/predict", methods=["POST"])
def home():
    data1 = request.form['a']
    data2 = request.form['b']
    data3 = request.form['c']
    data4 = request.form['d']
    arr = np.array([[data1, data2, data3, data4]])
    pred = model.predict(arr)
    return render_template("after.html", data = pred)


if __name__ == "__main__":
    app.run(debug=True)