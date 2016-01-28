#program that will sum the numbers from 0 to 100
if __name__ == '__main__': # if this was the file called, ie not imported
	currentSum = 0 # variable initialization
	for i in range(0,101): # for loop from 0 to 100
		currentSum += i # add up i
	print(currentSum) # print to the screen