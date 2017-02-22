# Creates a pdf report of OCR data. Input: a csv following the standardized format defined by the OCR. Output: a pdf
# report showing the rates of discipline and attendance, grouped by demographic, with threshhold rates highlighted.

import pandas as pd
import sys

# Returns name of data file to be used based on command line args or user input
def acquireFileName():
	if len(args) > 1:
		filename = args[1]
	else:
		filename = raw_input("Enter file name: ")
	return filename

filename = acquireFileName()