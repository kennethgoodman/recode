#program that will sum the numbers from 1 to 100
if __name__ == '__main__': # if this was the file called, ie not imported
	theSum = 0 # variable initialization
	for i in range(1,101): # for loop from 1 to 100
		theSum += i # add up i
	print(theSum) # print to the screen