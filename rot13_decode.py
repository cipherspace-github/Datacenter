#!/usr/bin/python3

import codecs

s = input("Message do Decode here:")
print(codecs.decode(s, "rot-13"))