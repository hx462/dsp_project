from flask import Flask
from flask import render_template
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
	return render_template("base.html")

@app.route('/load/samples')
def samples(fft=None):
	i = 0
	n = 0

	while n < 3:
		avg_fft[n] = savevoice.savevoice(n)
		#print"The average is ", avg_fft[n]
		n = n + 1
	return render_template("samples.html", fft=avg_fft)


max_sound = max(avg_fft)

min_sound = min(avg_fft)

mid_sound = (max_sound + min_sound)/2


print "The maximum bound is ", max_sound
print "The medium bound is ", mid_sound
print "The minimum bound is ", min_sound

print "\nReady to start? make some sound"

@app.route('/load1/comb')
def comb(fftsamp=None):
	i = 0
	avg_comb = [0 for c in range(2)]
	while i < 2:
		avg_comb[i] = savecombination.savecombination(i)
		i = i + 1
	return render_template("comb.html", fftsamp=avg_comb)

@app.route('/words')
def words():
	savetransc.savetransc()
	return render_template("words.html")

@app.route('/words/transc')
def transc():
	import transcribe
	transcribe.transcribe()
	return render_template("transc.html")

@app.route('/load')
def load():
	return render_template("load.html")

@app.route('/load1')
def load1():
	return render_template("load1.html")

if __name__ == "__main__":
	app.run(debug=True)
