# -*- coding: utf-8 -*-

import string
import random
# Generates Random Alpha-Numeric string
# Given Size
__lenght = 48

def generator(size=__lenght, chars=string.ascii_uppercase + string.digits):
   return ''.join(random.choice(chars) for _ in range(size))
# temp variable for further use
temp = generator()
print(temp)
