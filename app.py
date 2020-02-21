# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 17:59:17 2020
@author: lorenzo 
"""
from flask import Flask, render_template, request, json
import matplotlib as plt
from Siamese_Network import main
from keras import backend as K
K.clear_session()

app = Flask(__name__)

# Website routes
@app.route("/")
def userInterface():
	return render_template('UserInterface.html')

@app.route("/verify", methods=['POST'])
def verify():
	image1 = request.form['knownImage']
	image2 = request.form['unknownImage']
	
	knownImage = "karianne.jpg"
	unknownImage = "person1_makeup.jpg"
	result = main(knownImage,unknownImage)   
	
	return render_template('UserInterface.html', dataOut = result)

if __name__ == "__main__":
	app.run()
	