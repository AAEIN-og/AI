#3==============BFS=======================================
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
visited = [] #List to keep track of visited nodes
queue = []  #Initialize a queue

def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)
    
    while queue:
        s= queue.pop(0)
        print(s,end=" ")

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
#Driver code
bfs(visited,graph,'2')

#/3==========================================================
