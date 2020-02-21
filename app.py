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
	K.clear_session()
	return render_template('UserInterface.html')

@app.route("/verify", methods=['POST'])
def verify():
	knownImage = request.form.get('knownImage')
	unknownImage = request.form.get('unknownImage')
	imageResult = ''
	
	if knownImage and unknownImage:
		imageResult = main(knownImage,unknownImage) # verifies if image is within threshold and produces imageResult
		
	return render_template('UserInterface.html', dataOut = imageResult)

if __name__ == "__main__":
	app.run()
	