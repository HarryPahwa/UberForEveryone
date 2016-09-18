from flask import flash, redirect, render_template, request, session
from uber import app

from flask import jsonify 
import copy

import uberCall
access_code = ""
phonenumber = ""
# print(uberCall.getAuthenticationURL())
# from game.Board import board as b
# from game.connectfour import SBM as comp
# g = b()


# routes for startup, need to render start.html
@app.route("/")
@app.route("/startup", methods=['GET', 'POST'])
def start(): 
	return render_template('start.html', 
							title='UBER4EVERY1')


# route for callback
@app.route("/callback/", methods=['GET', 'POST'])
def callback(): 
	return render_template('callback.html', 
							title='UBER4EVERY1')

@app.route("/getAuth/", methods=['POST'])
def getAuth(): 
	print(uberCall.getAuthenticationURL())
	return jsonify(uberCall.getAuthenticationURL())

@app.route('/code_handback/', methods=['GET','POST'])
def keepCode(): 
	access_code = request.form['code']
	phonenumber = request.form['number']
	print(access_code)
	print("pn " + phonenumber)
	uberCall.beginTexting(access_code, phonenumber)
	return "hi"
