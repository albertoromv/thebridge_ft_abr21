from flask import Flask, render_template, request
import pickle
import numpy as np
import os

os.chdir(r'C:\Users\Admin\Documents\GitHub\thebridge_ft_abr21\5-Productivization\1-Flask\2-ML&Flask')



model = pickle.load(open('iri.pkl', 'rb'))

app = Flask(__name__)

@app.route("/", methods = ["GET"])
def home():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)