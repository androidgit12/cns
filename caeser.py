import string

def encrypt():
	pt = input("PT: ").lower().replace(" ","")
	key = int(input("KEY: "))

	ct = ""
	
	for ele in pt:
		ascii = ord(ele)
		ascii -= ord('a')
		ascii += key
		ascii %= 26
		ascii += ord('a')
		ct += chr(ascii)
		
	print("CT is: ",ct)
	
def decrypt():
	ct = input("CT: ").lower().replace(" ","")
	key = int(input("Key: "))
	letters = list(string.ascii_lowercase)
	pt = ""
	
	for ele in ct:
		ascii = ord(ele)
		ascii -= ord('a')
		ascii -= key
		ascii %= 26
		ascii += ord('a')
		pt += chr(ascii)
		
	print("PT is: ",pt)

while(1):
	c = int(input("Enter the choice: "))
	if c == 1:
		encrypt()
	elif c == 2:
		decrypt()
	else:
		break
		
