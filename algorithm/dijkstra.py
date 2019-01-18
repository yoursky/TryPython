
# 1. graph
graph = {}
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2

graph['a'] = {}
graph['a']['fin'] = 1

graph['b'] = {}
graph['b']['a'] = 3
graph['b']['fin'] = 5

graph['fin'] = {}

# 2. cost
infinity = float('inf')
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity

# 3.
parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents['fin'] = None

# 4.
processed = []

def find_lowest_cost_node():
    lnode = None
    lcost = infinity
    for n in costs:
        cost = costs[n]
        if cost < lcost and n not in processed:
            lcost = cost
            lnode = n
    return lnode

# BEGIN dijkstra
node = find_lowest_cost_node()
while node is not None:
    neighbors = graph[node]
    cost = costs[node]
    for nei in neighbors:
        new_cost = neighbors[nei] + cost
        if new_cost < costs[nei]:
            costs[nei] = new_cost
            parents[nei] = node

    processed.append(node)
    node = find_lowest_cost_node()

cur_node = 'fin'
path = cur_node
while cur_node != 'start':
    pa = parents[cur_node]
    path = pa + ' -> ' + path
    cur_node = pa

print 'dijkstra found the shortest path:' + path
