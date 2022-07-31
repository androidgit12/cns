import random

q = int(input("Enter prime number: "))
a = int(input("Enter the primitive root of q: "))

xa = 36#random.randint(1, q)
xb = 58#random.randint(1, q)
print("Private key of A is: {} and private jey of B is: {}".format(xa, xb))

ya = pow(a,xa) % q
yb = pow(a,xb) % q
print("Public key of A is: {} and public key for B is: {}".format(ya, yb))


ka = pow(yb,xa) % q
kb = pow(ya,xb) % q
print("Shared secret key are: {} and {}".format(ka, kb))
