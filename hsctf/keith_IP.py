"""
The encrypted flag only consisted of hex characters.
So by encrypting all possible characters we can
save them into a dictionary with the original
form as values, this way we can decrypt the given data.
"""
#all possible hex
posHex = "abcdefghijklmnopqrstuvwxyz0123456789"
#dictionary with key = encrypted character, value = character unencrypted
dictionary = {}
for c in posHex:
	print c + " being encrypted"
	enc = chr(ord(c) ^ ((ord(c) >> 4))) #character encrypted
	print enc + " encrypted"
	dictionary[enc]=c
	


solution = ""
for c in "2004e3bcbcgbdcc`2004`27:2004`27:bcgbdcc`":
	solution += dictionary[c]

print solution
