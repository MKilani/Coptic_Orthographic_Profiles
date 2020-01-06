# -*- coding: utf-8 -*-
from copticPanDialect_1_0 import parseCopticPanDialect

#test PanDialect profile

print ()
print ("* =====")
print ("* Parse: ⲃⲣⲕⲟⲟⲩⲧ")
print ("* Parser: copticPanDialect_1_0")
print ("* =====")

verbose = True
wordToParse = "ⲃⲣⲕⲟⲟⲩⲧ"

print ()
print ("Results:")
print ()

parsedWord = parseCopticPanDialect(wordToParse, verbose)

print ()
print ("As a dictionary:")
print ()

print (parsedWord)

print ()
print ("------")

from copticSahidic_1_0 import parseCopticSahidic

#test Sahidic profile

print ()
print ("* =====")
print ("* Parse: ϣⲓⲕⲉ")
print ("* Parser: copticSahidic_1_0")
print ("* =====")

verbose = True
wordToParse = "ϣⲓⲕⲉ"

print ()
print ("Results:")
print ()

parsedWord = parseCopticSahidic(wordToParse, verbose)

print ()
print ("As a dictionary:")
print ()

print (parsedWord)

