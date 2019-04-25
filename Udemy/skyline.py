def myfunc(myString):
	myList = list(myString)
	for x in range(len(myList)):
		if x%2 == 0:
			myList[x] = myList[x].lower()
		else:
			myList[x] = myList[x].upper()

	return ''.join(myList)