# -*- coding: utf-8 -*-
"""Re.findall() & Re.finditer().ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1kaH9M3V_wYjsZ4x2xsEzKl03JcTze3Og
"""

import re
Storage = re.findall(r'(?<=[qwrtypsdfghjklzxcvbnm])([aeiou]{2,})(?=[qwrtypsdfghjklzxcvbnm])', input().strip(), re.IGNORECASE)
if Storage:
    for i in Storage:
        print(i)
else:
    print(-1)