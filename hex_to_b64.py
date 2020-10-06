#!/usr/bin/python3
import codecs

hex = input("Hex:")
b64 = codecs.encode(codecs.decode(hex, 'hex'), 'base64').decode()
print(b64)