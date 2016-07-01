#!/usr/bin/env python3
"""
Figure flaming generated by HiST program
Michael Hirsch
"""
from __future__ import division,absolute_import
from sys import argv
from matplotlib.pyplot import show
#
from histfeas.main_hist import doSim
from histfeas.loadAnalyze import readresults,findxlsh5

def hist_figure():
    Phi0,Phifit =doSim(ParamFN=regXLS,
                  makeplot=['fwd','optim','png','h5'],
                  timeInds=timeInds,
                  overrides = overrides, #{'minev': minev,'filter':filt, 'fwdguess':fwdguess,
				                    #'fitm':fitm,'cam':cam,'camx':acx,'ell':ell,'Jfwd':influx},
                  odir = outdir,
                  x1d=x1d,
                  vlim = vlim,
                  animtime=None,
                  cmd = ' '.join(argv),
                  verbose=0
                  )

    return Phi0,Phifit


if __name__ == '__main__':
    from argparse import ArgumentParser
    p = ArgumentParser(description='flaming figure plotter')
    p.add_argument('--load',help='load without recomputing',action='store_true')
    p.add_argument('-m','--makeplot',help='plots to make',default=[],nargs='+')
    p.add_argument('--ell',help='compute projection matrix',action='store_true')
    p.add_argument('-v','--verbose',help='verbosity',action='count',default=0)
    p.add_argument('-f','--frames',help='time steps to use',type=int,default=(0,2,4,6))
    p = p.parse_args()

    regXLS='in/2cam_flame_xsweep.xlsx'
    timeInds=p.frames
    outdir='~/data/out/rev2_flame2_xsweep'
    x1d = [3.7,3.7,6,6]
    vlim = {'p':[-1.5,7.5,90,300,5e7,8e8,5e7,2e9], 'j':[1e3,2e4, 1e3,8e5],
            'b':[0,1.5e3]}
    overrides = {'ell':p.ell}

    if not p.load:
        print('running Hist program -- will write png and h5 to ' + outdir)
        Phi0,Phifit=hist_figure()


    h5list,xlsfn = findxlsh5(outdir)
    readresults(h5list,xlsfn,vlim,x1d,overrides,p.makeplot,p.verbose)

    if 'show' in p.makeplot:
        show()