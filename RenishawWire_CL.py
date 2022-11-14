#!/usr/bin/env python3


from renishawWiRE import WDFReader
import numpy as np
import pandas as pd

name = input('File name: ')

def read_wdf(name):
	reader = WDFReader(name)
	spectra = reader.spectra
	shp = spectra.shape

	wn = reader.xdata
	data = spectra.reshape(shp[0]*shp[1], len(wn))
	return data

y = np.array(read_wdf(name))
y = np.savetxt("DataMatrix.csv", y, delimiter=",")
