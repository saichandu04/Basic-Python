# -*- coding: utf-8 -*-
"""Validating Roman Numerals.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kaH9M3V_wYjsZ4x2xsEzKl03JcTze3Og
"""

regex_pattern = r""	
thousand = 'M{0,3}'
hundred = '(C[MD]|D?C{0,3})'
ten = '(X[CL]|L?X{0,3})'
digit = '(I[VX]|V?I{0,3})'
regex_pattern = r"%s%s%s%s$" % (thousand, hundred, ten, digit)    
import re
print(str(bool(re.match(regex_pattern, input()))))