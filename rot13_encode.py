#!/usr/bin/python3

import codecs

s = input("Message do Encode here:")
print(codecs.encode(s, "rot-13"))