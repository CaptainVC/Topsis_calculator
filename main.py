from django.shortcuts import render
from flask import Flask, flash, render_template, request
from mailsender import send_mail
from topsis import build_topsis
import pandas as pd

app = Flask(__name__)

@app.route('/', methods = ["GET", "POST"])

def main_page():
    if request.method == "POST":
        inputFile = request.files['inputcsv']
        weights = [int(x) for x in request.form['weight'].split(',')]
        impacts = request.form['impact'].split(',')
        emailid = request.form['emailid']
        df = pd.read_csv(inputFile)
        build_topsis(df, weights, impacts)
        send_mail(emailid)
        
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug = True, port = 8000)