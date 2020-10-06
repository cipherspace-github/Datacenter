#!/usr/bin/python3


def xor_byte_strings(byte_1, byte_2):
	return bytes([b1 ^ b2 for b1, b2 in zip(byte_1, byte_2)])

def main():
	Input_A = input("Hex String 1:")
	Input_B = input("Hex String 2:")
	byte_string_1 = bytes.fromhex(Input_A)
	byte_string_2 = bytes.fromhex(Input_B)
	print(xor_byte_strings(byte_string_1, byte_string_2).hex())


main()