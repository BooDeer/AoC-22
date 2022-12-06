print("Begining of the program: ")

with open("input.txt") as file:

	data = file.readlines()
	finalScore = 0
	group = []
	for line in data:
		group.append(line.rstrip())
		if (len(group) == 3):
			if common := next(iter(set.intersection(*map(set,group)))) : # if any of the characters in the second half are in the first half
				if common >= 'a':
					finalScore += ord(common) - 96
				else:
					finalScore += ord(common) - 38
			group = []

		
	print(f"finalScore: {finalScore}")
print("End of the program.")