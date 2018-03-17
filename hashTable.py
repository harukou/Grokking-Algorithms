voted = {}
def ifVoted(name):
	if voted.get(name) == True:
		print(name,'Have voted, let them out!')
	else:
		voted[name] = True
		print('Let them in and vote!')

ifVoted('Tom')
ifVoted('Mike')
ifVoted('Tom')
ifVoted('Tim')
