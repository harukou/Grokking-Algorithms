from collections import deque

def person_is_seller(name):
	return name[-1] == 'e'
def search(name):
	search_queue = deque()
	search_queue +=  graph[name]
	searched = []
	while search_queue:
		person = search_queue.popleft()
		if person not in searched:
			if person_is_seller(person):
				print(person+' is a mango seller!')
				return True
			else:
				search_queue += graph[person]
			#the following stm can code in else and if-not-in
			searched.append(person)
	return False
graph = {}
graph['you'] = ['bob','alice','claire']
graph['bob'] = ['anuj','peggr']
graph['alice'] = ['peggr']
graph['claire'] = ['thom','jonny']
graph['anuj'] = []
graph['peggr'] = []
graph['jonny'] = []
graph['thom'] = []
search('you')