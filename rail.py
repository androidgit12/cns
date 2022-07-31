def encrypt():
	
	pt = input("Enter plaintext: ").lower().replace(" ","")
	key = int(input("Enter key: "))
	
	arr = [['\n' for j in range(len(pt))]for i in range(key)]
	
	row = 0
	col = 0
	down = False
	for i in range(len(pt)):
	
		if row == 0 or row == key - 1:
			down = not down
		
		arr[row][col] = pt[i]
		col += 1
		
		if down:
			row += 1
		else:
			row -= 1
	ct = ""		
	for i in range(key):
		for j in range(len(pt)):
			if arr[i][j] != '\n':
				ct += arr[i][j]
	print(ct)
	decrypt(ct, key)
				
def decrypt(cipher, key):

	arr = [['\n' for j in range(len(cipher))]for i in range(key)]
	
	down = False
	row = 0
	col = 0
	
	for i in range(len(cipher)):
		if row == 0 or row == key - 1:
			down = not down
		arr[row][col] = "*"
		col += 1
		if down:
			row += 1
		else:
			row -= 1
			
	index = 0
	for i in range(key):
		for j in range(len(cipher)):
			if arr[i][j] == "*":
				arr[i][j] = cipher[index]
				index += 1
	
	down = False
	row = 0
	col = 0
	for i in range(len(cipher)):
		if row == 0 or row == key-1:
			down = not down
		print(arr[row][col], end="")
		col += 1
		if down:
			row += 1
		else:
			row -= 1
			
encrypt()
