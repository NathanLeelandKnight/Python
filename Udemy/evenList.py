def myfunc(*args):
	mylist = []
	for x in args:
		if (x%2) == 0:
			mylist.append(x)

	return mylist

print(myfunc(2,3,4))

