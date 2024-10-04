from chemFunctions import *

def molarityFromGrams(el, liters, grams):
    return conversion(grams, el, "grams_to_moles")/liters

def molarityFromMoles(liters, moles):
    return moles/liters

def molalityFromGrams(el, liters, grams):
    return conversion(grams, el, "grams_to_moles")/liters