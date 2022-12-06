print("Begining of the program: ")

with open("input.txt") as file:

	data = file.readlines()
	finalScore = 0
	for line in data:
		firstpart, secondpart = line[:len(line)//2], line[len(line)//2:] # split the line in half
		if any((Match :=x) in firstpart for x in secondpart): # if any of the characters in the second half are in the first half
			if Match >= 'a':
				finalScore += ord(Match) - 96
			else:
				finalScore += ord(Match) - 38
		
		print(f"finalScore: {finalScore}")
print("End of the program.")