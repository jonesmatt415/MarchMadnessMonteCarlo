March Madness, Monte Carlo Style!
=================================

See the [original blog post](http://www.mglerner.com/blog/?p=16).

Generate a single bracket for the South, using the default energy
function, and a temperature of 0.5 (given in units of epsilon/k):

```python
import MarchMadnessMonteCarlo as MMMC
teams = MMMC.teams['south']
b = MMMC.Bracket(teams=teams,T=0.5)
print b
```

Will print something like

```
Duke (1)                                                     
Robert Morris (16)        Duk (1)                            
San Diego St. (8)                                            
St. John's (9)            St. (9)  St. (9)                   
Utah (5)                                                     
Stephen F. Austin (12)    Uta (5)                            
Georgetown (4)                                               
Eastern Washington (13)   Geo (4)  Uta (5)  Uta (5)          
SMU (6)                   SMU (6)  Iow (3)  Gon (2)  Gon (2) 
UCLA (11)                                                    
Iowa St. (3)              Iow (3)                            
UAB (14)                                                     
Iowa (7)                  Iow (7)  Gon (2)                   
Davidson (10)                                                
Gonzaga (2)               Gon (2)                            
North Dakota St. (15)                                        
Total bracket energy: -18.3543040755
```

You use the default energy function by default (hey, maybe that's why
it's called "default"):

```python
from MarchMadnessMonteCarlo import RankingsAndStrength as RAS
strength = RAS.kenpom['Pyth']
def energy_game(winner, loser):
    """This is where you'll input your own energy functions. Here are
    some of the things we talked about in class. Remember that you
    want the energy of an "expected" outcome to be lower than that of
    an upset.
    """
    result = -(strength[winner]/strength[loser])
    return result
```

Most of the fun here comes from replacing that with your own energy
function. For instance, you might want a difference rather than a
ratio:

```python
import MarchMadnessMonteCarlo as MMMC

from MarchMadnessMonteCarlo import RankingsAndStrength as RAS
strength = RAS.kenpom['Pyth']
def my_energy_game(winner,loser):
    result = -(strength[winner] - strength[loser])
    return result

MMMC.set_energy_function(my_energy_game)
teams = MMMC.teams['south']
b = MMMC.Bracket(teams=teams,T=0.5)
print b
```

Having done that, as described in the blog post, there are a few
different ways you might want to simulate several runs:


```python
import MarchMadnessMonteCarlo as MMMC  
MMMC.simulate(1000,'south',0.5)
```

or full brackets:

```python
import MarchMadnessMonteCarlo as MMMC  
MMMC.simulate(1000,'all',0.5)
```

your own final four:

```python
import MarchMadnessMonteCarlo as MMMC
MMMC.simulate(1000,['Louisville','Gonzaga','Kansas','Indiana'],0.5)
```

or the two full bracket wrappers described in the blog post:

```python
import MarchMadnessMonteCarlo as MMMC
MMMC.runbracket1(ntrials=10000,T=1.0)
```

```python
import MarchMadnessMonteCarlo as MMMC
MMMC.runbracket2(ntrials1=10000,ntrials2=1000,T=1.0)
```

