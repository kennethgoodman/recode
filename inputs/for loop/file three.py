#program that will sum the numbers from 7 to 84
if __name__ == '__main__': # if this was the file called, ie not imported
	currentSum = 0 # variable initialization
	for i in range(7,84): # for loop from 7 to 84
		currentSum += i # add up i
	print(currentSum) # print to the screen