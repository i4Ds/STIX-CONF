from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
import itertools
import pylab as plb
from scipy.optimize import curve_fit
from scipy.signal import find_peaks
from scipy.signal import convolve
import scipy.interpolate
import scipy.ndimage
import sys
sys.path.insert(0, "/Users/ol161303/Documents/PROGRAMMES/IDL-DATA/prog_idl/02_STIX/PIPELINE/V_20200412/STX_Mac/PYTHON_LIB")
from STIX_Lib import *
from scipy import stats
import math as math
import csv


#open  csv files and sum them up
PATH_FILES = "/Users/ol161303/Documents/PROGRAMMES/IDL-DATA/prog_idl/02_STIX/PIPELINE/V_20200412/STIX/RAW_DATA/01_CSV/2024/01_JAN_/"

Run_numbers = ["2890", "2892"]



#array to store and sum the spectra of each channels ie, each line of csv (recombined subspec by Hugo)
S = np.zeros((384, 1019), dtype=int) #generate an empty integer array 384 pixels, 1019 energy bins from calibration files
for Run_number in Run_numbers:
    Counter = 0
    print("Current Run Number to be processed: ", Run_number)
    CSV_FILE = PATH_FILES + "calibration_run_" + Run_number + "_all.csv"
    with open(CSV_FILE, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            results = np.array([int(i) for i in row])
            S[Counter, :] += results
            Counter += 1

#Now writes the sum in a unique csv to be processed (fits, calibration application, ...)
#Change S into list mode for csv writing
S_list = S.tolist()

FileOut = PATH_FILES + "calibration_run_13131313131313_all.csv"
f = open(FileOut, 'w')
with f:
    writer = csv.writer(f)
    for row in S_list:
        writer.writerow(row)






