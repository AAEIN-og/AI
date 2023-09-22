#5================dfs========
graph={
    '2':['7','5'],
    '7':['2','10','6'],
    '5':['9'],
    '10':[],
    '6':['5','11'],
    '9':['4'],
    '11':[],
    '4':[],
    }

visited = set()

def dfs(visited,graph,node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited,graph,neighbour)

#Function
dfs(visited,graph,'2')

#5==========================
