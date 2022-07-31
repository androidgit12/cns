def encrypt(PR, PU, n):
	m = int(input("Enter PT: "))
	c = pow(m, PU, n)
	print("Cipher text is: {}".format(c))
	decrypt(PR, PU, n, c) 
	
def decrypt(PR, PU, n, c):
	m = pow(c, PR, n)
	print("Plain text is: {}".format(m))
	print("")

def gcd(a, b):
	if b == 0:
		return a
	return gcd(b, a%b)

p = int(input("Enter p: "))
q = int(input("Enter q: "))

n = p * q
totient = (p-1) * (q-1)

#e
e = 7
while(e > totient):
	if( gcd(e, totient) == 1 ):
		break
	else:
		e += 1
print("Public key is: ",e)


#d
d = 1
while(1):
	if((d * e) % totient) == 1:
		break
	else:
		d += 1
	
print("Private key is: ",d)

PR = d
PU = e

encrypt(PR, PU, n)
