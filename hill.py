import string
import numpy as np

letters = list(string.ascii_lowercase)

def sameSize(pt, n):
	while len(pt) % n != 0:
		pt += 'z'
	return pt
	
def multiply(key, arr, n):
	arr1 = []
	for i in range(n):
		sum1 = 0
		for j in range(n):
			sum1 += (round(key[i][j]) * arr[j]) 
		arr1.append(sum1%26)
	return arr1

def encrypt():

	pt = input("Enter the plaintext: ").replace(" ","").lower()
	n = int(input())
	key = [[int(j) for j in input().split()]for i in range(n)]
	ct = ""
	
	pt = sameSize(pt, n)
	
	for i in range(0, len(pt), n):
		arr = []
		for j in range(i, i+n):
			arr.append(letters.index(pt[j]))
		cipherArr = multiply(key, arr, n)
		for j in range(n):
			ct += letters[cipherArr[j]]
	print("Ciphertext is: ",ct)
	decrypt(ct, key, n)
	
def decrypt(ct, key, n):
	pt = ""
	
	
	key = np.array(key)
	
	det = np.linalg.det(key)
	
	invKey = np.linalg.inv(key)
	
	for i in range(n):
		for j in range(n):
			invKey[i][j] *= det
			invKey[i][j] %= 26
			if invKey[i][j] < 0:
				invKey[i][j] += 26
	
	det %= 26
	if det < 0:
		det += 26
		

	print(invKey)
	k = 1
	while(1):
		print(round((det * k)) % 26)
		if round((det * k)) % 26 == 1:
			print(k)
			break
		else:
			k += 1
	
	for i in range(n):
		for j in range(n):
			invKey[i][j] *= k
			invKey[i][j] %= 26
			if invKey[i][j] < 0:
				invKey[i][j] += 26
				
	key = invKey
	print(key)
	
	
	
	for i in range(0, len(ct), n):
		arr = []
		for j in range(i, i+n):
			arr.append(letters.index(ct[j]))
		plainArr = multiply(key, arr, n)
		for j in range(n):
			pt += letters[plainArr[j]]
	print("Plaintext is: ",pt)


encrypt()
