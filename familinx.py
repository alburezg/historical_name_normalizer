# -*- coding: utf-8 -*-
"""
Created on Wed Jun 19 13:14:11 2019

@author: AlburezGutierrez
"""

import os
import io

"""
Familinx example
"""

"""
Load data
"""

# For interactive use only
pd = os.getcwd()
pd = 'C:\\Cloud\\Projects\\Sweden\\historical_name_normalizer'

# pd = os.path.dirname(os.path.abspath(__file__)) 
fname = os.path.join(pd, 'data', 'cause_of_death.txt')

data = io.open(fname, 'r', encoding = 'utf8')

print data.read()

# Normalise names

cause_death_normalizer = NameNormalizer('cause_of_death')

cod = 'hjartattack'
    print u"\nCasue of death to normalize: {}\n".format(cod)
    normalized = cod_normalizer.normalize(cod)
    print u"Normalized: {}\n".format(normalized)