import math
import random

def random_number_generator(): 
    sets = set(())

    for x in range(10):
       sets.update("{}".format(math.floor(random.random()* 100)))
    return sets

def findExtremeValues(): 
    sets = random_number_generator()
    print("From {}: smallest: {} , largest: {}".format( sets, min(sets), max(sets)))


findExtremeValues()