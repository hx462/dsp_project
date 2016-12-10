from flask import Flask
from flask import render_template
from flask import jsonify
from flask import request
import pyaudio
import struct
import wave
import datetime
import numpy as np
from matplotlib import pyplot as plt
from myfunctions import clip16, matchwords
import pyttsx
import operator
import savevoice
import savecombination
import datetime
import savetransc
import time


app = Flask(__name__)
fft_sum = 0
global avg_fft
avg_fft = [0 for a in range(3)]



@app.route('/')
def bottoms():
	return render_template("index.html")

@app.route('/recording')
def recording():
	print "\nReady to start? make some sound"

	return render_template("recording.html")

# Call the function to record data and return json data to jQuery
# so as to display on the web page
@app.route('/recording_data')
def samples(fft=None):
	n = 0

	while n < 3:
		avg_fft[n] = savevoice.savevoice(n)
		#print"The average is ", avg_fft[n]
		n = n + 1
	return jsonify(avg_fft1=avg_fft[0], avg_fft2=avg_fft[1], avg_fft3=avg_fft[2])


# def signUpUser():
#     user =  request.form['username'];
#     password = request.form['password'];
#     return json.dumps({'status':'OK','user':user,'pass':password});

max_sound = max(avg_fft)

min_sound = min(avg_fft)

mid_sound = (max_sound + min_sound)/2


print "The maximum bound is ", max_sound
print "The medium bound is ", mid_sound
print "The minimum bound is ", min_sound



@app.route('/combination')
def comb():
	return render_template("combination.html")


@app.route('/combination_data')
def comb_data(fftsamp=None):
	i = 0
	avg_comb = [0 for c in range(0, 2)]

	while i < 2:
		avg_comb[i] = savecombination.savecombination(i)
		i = i + 1
	return jsonify(avg_comb1=avg_comb[0], avg_comb2=avg_comb[1])


# @app.route('/test')
# def test():
# 	a, b = 0, 0
# 	return jsonify(test1=a, test2=b)


@app.route('/words')
def words():
	savetransc.savetransc()
	return render_template("words.html")

@app.route('/words/v2t')
def transc():
	import transcribe
	transcribe.transcribe()
	return render_template("v2t.html")

@app.route('/load')
def load():
	return render_template("load.html")

# @app.route('/load1')
# def load1():
# 	return render_template("load1.html")

if __name__ == "__main__":
	app.run(debug=True)
