import sys

"""  
Something to do with universe and Python
"""

name = sys.argv[1]

def UniverseMe(name, planet):
    pl = "Hi " + planet + " its me " + name + " saying hello from earth!"
    return pl

print (UniverseMe(name, "Saturn"))