print("Begining of the program: ")

with open("input.txt") as file:

	data = file.readlines()
	overlaps = 0
	for line in data:
		ranges = line.rstrip('\n').split(",")
		firstRange = ranges[0].split("-")
		secondRange = ranges[1].split("-")
		# print(f"firstRange: {firstRange} secondRange: {secondRange}")
		if firstRange[0] <= secondRange[0] and firstRange[1] >= secondRange[1]:
			overlaps += 1
		elif firstRange[0] >= secondRange[0] and firstRange[1] <= secondRange[1]:
			overlaps += 1
	
	print(f"overlaps: {overlaps}")
print("End of the program.")