import sys
from testpy import testme, hellome
# this is just to trigger the change
"""  
Something to do with universe and Python

Lets add some details to this comment

Add more details.

Adding some additional details.
"""

name = sys.argv[1]
me = "Functional"

def UniverseMe(name, planet):
    pl = "Hi " + planet + " its me " + name + " saying hello from earth!"
    return pl

print (UniverseMe(name, "Saturn"))
print ()
testme()
hellome(me)
