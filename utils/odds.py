'''
Odds Utility Module

A light wrapper around random stuff, so we don't have to keep repeating formulae.
'''
import random

'''
The basic chance calculation.
Used primarily for determining if we get an epic item or rare mob.
'''
def basic(chance):
    return random.randrange(1, (1 + chance), 1)