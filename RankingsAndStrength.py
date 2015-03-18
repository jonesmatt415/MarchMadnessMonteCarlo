#!/usr/bin/env python
from __future__ import division
from collections import OrderedDict
import KenPomeroy as KP
import JeffSagarin as JS
import MarchMadnessMonteCarlo as MMMC
from numpy.random import random #import only one function from somewhere

kenpom = {}
for strength_type in KP.lineparts:
    kenpom[strength_type] = {}
    for team in MMMC.all_teams:
        kenpom[strength_type][team] = KP.kpomdata[team][strength_type]


sagarin = {}
sagarin['Rating'] = {}
sagarin['Rank'] = {}
for team in MMMC.all_teams:
    sagarin['Rating'][team] = JS.sagarindata[team]['Rating']
    sagarin['Rank'][team] = JS.sagarindata[team]['Rank']

