#!/usr/bin/env python

import MarchMadnessMonteCarlo as MMMC
from MarchMadnessMonteCarlo import RankingsAndStrength as RAS
regional_rankings = MMMC.regional_rankings
strength = RAS.kenpom['Pyth']

def default_energy_game(winner, loser):
    """This is where you'll input your own energy functions. Here are
    some of the things we talked about in class. Remember that you
    want the energy of an "expected" outcome to be lower than that of
    an upset.

    """
    result = -(strength[winner] - strength[loser])
    result = regional_rankings[winner] - regional_rankings[loser]
    result = regional_rankings[winner]/regional_rankings[loser]
    result = -(strength[winner]/strength[loser])
    #result = random()
    #result = color of team 1 jersey better than color of team 2 jersey
    #print "energy_game(",winner,loser,")",result
    return result

def log5_energy_game(winner, loser):
    A,B = strength[winner],strength[loser]
    # see http://207.56.97.150/articles/playoff2002.htm
    win_pct = (A-A*B)/(A+B-2*A*B)
    return -win_pct
