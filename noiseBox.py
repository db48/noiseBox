#!/usr/bin/python -tt

import sys
import numpy
import scipy
import random
import matplotlib
import matplotlib.pyplot as plt


def uniformDist(length_sec, fs):
	print 'uniform distribution chosen (%d %d)' % ( length_sec, fs )
	nsamp = fs*length_sec
	return numpy.random.uniform(0,fs/2,nsamp)

def gaussDist(length_sec, fs):
	print 'gaussian distribution chosen' + ' ' + str(length_sec) + ' ' + str(fs)
	nsamp = fs*length_sec
	return numpy.random.normal(fs/4,fs/8,nsamp)

def rayleighDist(length_sec, fs):
	print 'gaussian distribution chosen' + ' ' + str(length_sec) + ' ' + str(fs)
	nsamp = fs*length_sec
	return numpy.random.rayleigh(fs/4,nsamp)

def printErrorBadRandomGen(length_sec, fs):
	# note the trailing comma here which suppresses the newline
	print 'undfined random value generator, using uniform ',
	return uniformDist(length_sec,fs)

def createNoise(lentgh_sec, fs, tone, noiseAlpha, noiseDist):
	noiseDict = {
		0: uniformDist,
		1: gaussDist,
		2: rayleighDist,
	}
	func = noiseDict.get(noiseDist, printErrorBadRandomGen)
	freqContent = func(lentgh_sec, fs)
	return fft(freqContent)


# Define a main() function that prints a little greeting.
def main():
	# Get the name from the command line, using 'World' as a fallback.
	if len(sys.argv) >= 2:
		name = sys.argv[1]
	else:
		name = 'World'
	print 'Howdy', name, '!'

	# some plot setup
	fig, ax = plt.subplots(3,1)

	for i in range(3) :
		x1 = createNoise(10, 1000, 'a', 1.0, i)
		ax[i].hist(x1,100)
		ax[i].grid()

	plt.show()

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
	main()
