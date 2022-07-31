import string

def encrypt():
	
	pt = input("Enter the plaintext: ").lower().replace(" ","")
	key = input("Enter the key: ").lower().replace(" ","")
	ct = ""
	letters = list(string.ascii_lowercase)
	
	ki = 0
	
	for i in range(len(pt)):
		li = ( letters.index(pt[i]) + letters.index(key[ki % len(key)]) ) % 26
		ki += 1
		ct += letters[li]
	print("Ciphertext is: ",ct)
	decrypt(ct, key)
	
	
def decrypt(ct, key):
	
	pt = ""
	letters = list(string.ascii_lowercase)
	
	ki = 0
	
	for i in range(len(ct)):
		li = ( letters.index(ct[i]) - letters.index(key[ki % len(key)]) ) % 26
		ki += 1
		pt += letters[li]
	print("Plaintext is: ",pt)

while(1):
	ch = input("Choice: ")
	if ch == "1":
		encrypt()
	else:
		break
