# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 17:59:17 2020

@author: lorenzo 
"""

from flask import Flask, render_template, request, json
from Siamese_Network import main

app = Flask(__name__)


# Website routes
@app.route("/")
def userInterface():
	return render_template('UserInterface.html')

@app.route("/verify", methods=['GET','POST'])
def verify():
	knownImage = request.form['knownImage']
	unknownImage = request.form['unknownImage']
	result = main(knownImage,unknownImage)
	return render_template('UserInterface.html', dataOut = result)

if __name__ == "__main__":
	app.run()
	