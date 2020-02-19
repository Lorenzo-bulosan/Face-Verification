# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 17:59:17 2020

@author: lorenzo 
"""

from flask import Flask, render_template, request

app = Flask(__name__)

# Website routes
@app.route("/")
def userInterface():
	return render_template('UserInterface.html')

@app.route("/verify", methods=['GET','POST'])
def verify():
	dataIn = '0'
	if request.method == 'POST':
		dataIn = request.json['data']
	return render_template('UserInterface.html',dataOut=str(dataIn))

if __name__ == "__main__":
	app.run()
	