print("Begining of the program: ")

with open("input.txt") as file:
	numberOfElves = 1
	caloriesList = []
	maximumCalories = 0
	caloriesPerElf = 0

	data = file.readlines()
	for line in data:
		# print(line, end="")
		if not line.strip():
			# print("Empty line number: ", numberOfElves)
			numberOfElves += 1
			caloriesList.append(maximumCalories)
			caloriesPerElf = 0
		else:
			caloriesPerElf += int(line)
			if caloriesPerElf > maximumCalories:
				maximumCalories = caloriesPerElf


print(f"Maximum calories: {maximumCalories}")
print("End of the program.")