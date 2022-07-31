import string

def seperateSameLetters(pt):
	i = 0
	updatePt = ""
	while i < len(pt):
	
		if i == len(pt) - 1:
			updatePt += pt[i]
			break
		
		if pt[i] == pt[i+1]:
			updatePt += pt[i]
			updatePt += 'x'
			i += 1
		else:
			updatePt += pt[i]
			updatePt += pt[i+1]
			i += 2
			
	return updatePt
	
def evenPt(pt):
	if len(pt) % 2 != 0:
		pt += 'z'
	return pt
	
def generateKeyTable(key):
	letters = list(string.ascii_lowercase)
	letters.remove("j")
	
	arr = [["" for j in range(5)]for i in range(5)]
	
	visited = [""] * 26
	
	r = 0
	c = 0
	for ele in key:
		if ele not in visited:
			arr[r][c] = ele
			visited.append(arr[r][c])
			if c == 4:
				r = (r + 1) % 5
				c = 0
			else:
				c = (c + 1) % 5
				
	for ele in letters:
		if ele not in visited:
			arr[r][c] = ele
			visited.append(arr[r][c])
			if c == 4:
				r = (r + 1) % 5
				c = 0
			else:
				c = (c + 1) % 5
	return arr
	
def find(s, keyTable):
	r1, c1, r2, c2 = 0, 0, 0, 0
	
	for i in range(5):
		for j in range(5):
			if keyTable[i][j] == s[0]:
				r1 = i
				c1 = j
			elif keyTable[i][j] == s[1]:
				r2 = i
				c2 = j
			
	
	return r1, c1, r2, c2

def getCipher(d, keyTable):

	r1, c1, r2, c2 = find(d, keyTable)
	updatedD = ""
	if r1 == r2:
		updatedD += keyTable[r1][(c1+1) % 5]
		updatedD += keyTable[r1][(c2+1) % 5]
	elif c1 == c2:
		updatedD += keyTable[(r1+1) % 5][c1]
		updatedD += keyTable[(r2+1) % 5][c1]
	else:
		updatedD += keyTable[r1][c2]
		updatedD += keyTable[r2][c1]
	return updatedD
		

pt = input("Enter the plaintext: ").lower().replace(" ","").replace("j", "i")
key = input("Enter the key: ").lower().replace(" ","").replace("j", "i")

pt = seperateSameLetters(pt)
pt = evenPt(pt)
print(pt)

keyTable = generateKeyTable(key)
print(keyTable)

ct = ""

for i in range(0, len(pt), 2):
	d = []
	d += pt[i] 
	d += pt[i+1]
	ctD = getCipher(d, keyTable)
	ct += ctD
	
print(ct)
