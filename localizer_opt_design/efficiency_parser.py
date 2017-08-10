#!/usr/bin/env python
import re #regex module
import numpy as np
import sys

#Usage: efficiency_parser.py out.txt
#Parse the output of 3dDeconvole -nodata stored in out.txt


#make a dictionary to store the results
results_stim = {'Stimulus': [], 'eff': []}
results_cont = {'Contrast': [], 'eff': []}

#open the 3dDeconvolve output filename stored in sys.argv[1]
#read all the lines in the file into a string s. 
with open(sys.argv[1], 'r') as f:
    s=f.read()

#compile the regex
#use re.MULTILINE since we need to match across lines
p_stimulus = re.compile(r"^Stimulus:\s+(.+)\s+.+ ([.0-9]+)", re.MULTILINE)
p_contrast = re.compile(r"^General Linear Test:\s+(.+)\s+.+ ([.0-9]+)", re.MULTILINE)

#find all of the matches in s and return an interator in matches
matches_s = p_stimulus.finditer(s)
matches_c = p_contrast.finditer(s)

#TODO: iterate through matches and copy the values to the results dictionary
#for each match, m, you get from the iterator, m.groups() is a tuple
#try m=p.search() to see what the first one looks like
for m in matches_s:
	results_stim['Stimulus'].append(m.groups()[0])
	results_stim['eff'].append(float(m.groups()[1]))

for m in matches_c:
	results_cont['Contrast'].append(m.groups()[0])
	results_cont['eff'].append(float(m.groups()[1]))

#TODO: calculate the summed efficiency of all the stimulus functions and contrasts (i.e. sum the 'eff' key in the dictionary)
#try np.sum()
stim_eff_sum = np.sum(results_stim['eff'])
cont_eff_sum = np.sum(results_cont['eff'])

#TODO print the summed efficiency
print "%.3f %.3f" %(stim_eff_sum, cont_eff_sum)

