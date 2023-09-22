#2==============BFS=======================================
graph={
    'A':['B','C'],
    'B':['C','D'],
    'C':['E'],
    'D':['F'],
    'E':['F'],
    'F':[],
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
bfs(visited,graph,'A')

#/2==========================================================
