def applyTable(a, P):
	print("Apply permutation: ",a, P,end="->")
	res = ""
	for ele in P:
		res += a[ele-1]
	print(res)
	return res
	
def shift(a):
	print("Apply shift: ",a[1:] + a[0])
	return a[1:] + a[0]

def xor(a, key):
	res = ""
	for i in range(len(key)):
		if a[i] == key[i]:
			res += '0'
		else:
			res += '1'
	return res
def toBin(a):
	if a == "00":
		return 0
	elif a == "01":
		return 1
	elif a == "10":
		return 2
	else:
		return 3
def toDig(a):
	if a == 0:
		return "00"
	elif a == 1:
		return "01"
	elif a == 2:
		return "10"
	else:
		return "11"

def sbox(s0, a):
	row = a[0] + a[-1]
	col = a[1] + a[2]
	row = toBin(row)
	col = toBin(col)
	ele = s0[row][col]
	return toDig(ele)
	

def function(pt, k1, s0, s1, EP, P4):
	left = pt[:4]
	right = pt[4:]
	temp = applyTable(right, EP)
	temp = xor(temp, k1)
	left = temp[:4]
	right = temp[4:]
	lsbox = sbox(s0, left)
	rsbox = sbox(s1, right)
	temp = lsbox + rsbox
	temp = applyTable(temp, P4)
	temp = xor(temp, pt[:4])
	return temp + pt[4:]

P10=[3,5,2,7,4,10,1,9,8,6]
P8=[6,3,7,4,8,5,10,9]
IP=[2,6,3,1,4,8,5,7]
EP=[4,1,2,3,2,3,4,1]
P4=[2,4,3,1]
IPi=[4,1,3,5,7,2,8,6]
s0=[[1, 0, 3, 2], [3, 2, 1, 0], [0, 2, 1, 3], [3, 1, 3, 2]]
s1=[[0, 1, 2, 3], [2, 0, 1, 3], [3, 0, 1, 0], [2, 1, 0, 3]]

key = input("Enter a 10-bit key: ")
pt = input("Enter a 8-bit plaintext: ")

#Key
temp = applyTable(key, P10)
left = temp[:5]
right = temp[5:]
left = shift(left)
right = shift(right)
k1 = applyTable(left+right, P8)

left = shift(left)
right = shift(right)
left = shift(left)
right = shift(right)
k2 = applyTable(left+right, P8)

print("Keys are: ",k1, k2)

#Encrypt
temp = applyTable(pt, IP)
temp = function(temp, k1, s0, s1, EP, P4)
temp = temp[4:] + temp[:4]
temp = function(temp, k2, s0, s1, EP, P4)
ct = applyTable(temp, IPi)
print("Cipher text is: ",ct)

#DEcrypt
temp = applyTable(ct, IP)
temp = function(temp, k2, s0, s1, EP, P4)
temp = temp[4:] + temp[:4]
temp = function(temp, k1, s0, s1, EP, P4)
temp = applyTable(temp, IPi)
print("Plain text is: ",temp)
