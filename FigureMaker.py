#!/usr/bin/env python
"""
Figures of flaming aurora generated by HiST program

intended for use with in/ files including:
*_flame.ini
*_impulse.ini
*_trans.ini

Flaming Aurora 2 cameras:
python FigureMaker.py in/2cam_flame.ini

Translating Aurora 2 cameras:
python FigureMaker.py in/2cam_trans.ini

Impulse Aurora (for testing):
python FigureMaker.py in/2cam_impulse.ini

Table of results for 2 and 3 cam:
python FigureMaker.py in/table_flame{2,3}.py

"""
from histfeas import userinput, hist_figure
from histfeas.loadAnalyze import readresults,findxlsh5

P = userinput()
#%% compute
if not P['load']:
    hist_figure(P)
#%% load
flist,P = findxlsh5(P)
readresults(flist,P)
