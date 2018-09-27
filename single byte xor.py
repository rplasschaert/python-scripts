import binascii

encoded = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
strings = binascii.unhexlify(encoded)


for key in range(256):
	decoded = []
	
	for string in strings:
		xorred = chr(ord(string) ^ key)
		decoded.append(xorred)
		dec = ''.join(decoded)
	print(hex(key))		
	print(dec)		
		
	
