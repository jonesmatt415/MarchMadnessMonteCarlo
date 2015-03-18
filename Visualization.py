#!/usr/bin/env python
from __future__ import division
import numpy as np
from matplotlib import pyplot as plt
from random import choice, shuffle
from numpy.random import random #import only one function from somewhere
from numpy.random import randint
from numpy import exp, array, zeros, ones, convolve
import scipy
from time import sleep
from copy import deepcopy
from collections import Counter, OrderedDict

import RankingsAndStrength as RAS


def movingaverage(interval, window_size):
    window= ones(int(window_size))/float(window_size)
    return convolve(interval, window, 'same')

def plotone(brackets, label, subplot1, subplot2, values=None, label2=None, 
            values2=None, teamdesc=None, useavg=False):
    """
    Plotting too many points causes lots of trouble for matplotlib. At
    the moment, we deal with that by plotting at most 50000 points,
    skipping evenly through the data if needed.
    """
    maxpts = 50000

    ntrials = len(brackets)
    if values is None:
        try:
            values = [getattr(b,label)() for b in brackets]
        except TypeError:
            values = [getattr(b,label) for b in brackets]

    if len(values) >= 50000:
        step = divmod(len(values),maxpts)[0]
    else:
        step = 1
    
    plt.subplot(subplot1)
    plt.plot(xrange(0,ntrials,step),values[::step],'.',label=label)
    if useavg:
        # want something like 2000 windows
        if step > 1:
            npts = maxpts
        else:
            npts = len(values)
        avgstep = divmod(len(values),int(npts/25))[0]
        
        plt.plot(xrange(0,ntrials,step),movingaverage(values[::step],avgstep),'-',label='avg. '+label)
            
    plt.ylabel(label.capitalize())
    plt.xlabel('Game')
    if teamdesc is not None:
        plt.title('%s over the trajectory, T=%s, %s'%(label.capitalize(),
                                                     brackets[0].T,teamdesc))
    else:
        plt.title('%s over the trajectory, T=%s'%(label.capitalize(),
                                                 brackets[0].T))
    #plt.legend()
    plt.subplot(subplot2)
    if values2 is None:
        if ntrials > 1000:
            nbins = min(int(ntrials/100),200)
        else:
            nbins = 10
        plt.hist(values,bins=nbins)
        plt.title('%s distribution, T=%s'%(label.capitalize(), brackets[0].T))
    else:
        plt.subplot(subplot2)
        plt.plot(xrange(0,ntrials,step),values2[::step],'.',label=label2)
        plt.ylabel(label2.capitalize())
        plt.xlabel('Game')
        plt.title('%s over the trajectory, T=%s'%(label2.capitalize(),
                                                 brackets[0].T))

    
def showstats(brackets, unique_brackets, lowest_sightings, newfig=True,
              teamdesc=None,figsize=(15,8)):
    if newfig is not False:
        if newfig is True:
            plt.figure(figsize=figsize)
        else:
            plt.figure(newfig,figsize=figsize)
    plt.clf()
    plotone(brackets, 'energy', 231, 234, teamdesc=teamdesc)
    plotone(brackets, 'upsets', 232, 235, teamdesc=teamdesc)
    plotone(brackets, 'Unique brackets', 233, 236, values=unique_brackets,
            label2="Lowest Energy Sightings", values2=lowest_sightings,
            teamdesc=teamdesc)
    plt.show()

