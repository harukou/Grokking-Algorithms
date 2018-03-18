# the graph
graph = {}
graph['start'] = {}
graph['start']['a']=6
graph['start']['b']=2

graph['a'] = {}
graph['a']['end'] = 1

graph['b'] = {}
graph['b']['a'] = 3
graph['b']['end'] = 5

graph['end'] = {}
# the cost table
cost = {}
cost['a'] = 6
cost['b'] = 2
cost['end'] = float('inf') 
# the parents table 
parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['end'] = None
#processed array
processed = []

def find_lowest_cost_node(cost):
	lowest_cost = float('inf')
	lowest_cost_node = None
	for node in cost:
		cos = cost[node]
		if cos <lowest_cost and node not in processed:
			lowest_cost = cos
			lowest_cost_node = node
	return lowest_cost_node

node = find_lowest_cost_node(cost)
while node is not None:
	cost_= cost[node]
	neighbors = graph[node]
	for n in neighbors.keys():
		new_cost = cost_ + neighbors[n]
		if cost[n]>new_cost:
			cost[n] = new_cost
			parents[n] = node
	processed.append(node)
	node = find_lowest_cost_node(cost)

print(cost)
