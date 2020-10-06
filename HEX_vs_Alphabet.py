#!/usr/bin/python3
import codecs
import binascii

Hex = input("Hex:")

Charackters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]


for i in Charackters:
	Q = hex(ord(i))
	P = hex(int(Hex, 16) ^ int(Q, 16))
	T = P.decode("hex")
	print(i + "XOR =" + P)
	print(T)
	
	#P = hex(int(Hex, 16) ^ int(i, 16))
	#print(i + "XOR =" + P)