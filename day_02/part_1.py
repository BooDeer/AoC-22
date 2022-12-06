print("Begining of the program: ")

with open("input.txt") as file:

	data = file.readlines()
	finalScore = 0
	for line in data:
		enemyChoice = line.split()[0]
		myChoice = line.split()[1]
		match enemyChoice: # A ==> Rock || B ==> Paper || C ==> Scissors
			case "A":
				match myChoice:
					case "X":
						finalScore += 1 + 3
					case "Y":
						finalScore += 2 + 6
					case "Z":
						finalScore += 3 + 0
			case "B":
				match myChoice:
					case "X":
						finalScore += 1 + 0
					case "Y":
						finalScore += 2 + 3
					case "Z":
						finalScore += 3 + 6
			case "C":
				match myChoice:
					case "X":
						finalScore += 1 + 6
					case "Y":
						finalScore += 2 + 0
					case "Z":
						finalScore += 3 + 3
			case _:
				print("You chose something else.")
		
		print(f"finalScore: {finalScore}")
print("End of the program.")