# -*- coding: utf-8 -*-
"""Dot and Cross.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kaH9M3V_wYjsZ4x2xsEzKl03JcTze3Og
"""

import numpy
n = int(input())
a = numpy.array([input().split() for _ in range(n)], int)
b = numpy.array([input().split() for _ in range(n)], int)
print(numpy.dot(a, b))