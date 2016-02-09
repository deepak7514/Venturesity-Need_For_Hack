# Computing Strongly Connected Components in Directed Graph using Depth First Search

import sys
import time
import resource

# Increase recursion depth and stack size 
sys.setrecursionlimit(100000)
resource.setrlimit(resource.RLIMIT_STACK, (resource.RLIM_INFINITY, resource.RLIM_INFINITY))

def make_graph():
    """Make a graph and its transpose"""

    from collections import defaultdict
    e = int(raw_input('Enter number of edges: ')) # No of edges
    G = defaultdict(list) # construct an empty list of adjacent nodes for every vertex
    GT = defaultdict(list) # G's Transpose

    # Read edges and add them to the graphs

    d={} # Dictionary to map vertices to numbers starting from 1
    cnt=1
    for i in range(e):
        v1,v2 = map(int,raw_input().split())
        if not d.has_key(v1):
            d[v1]=cnt
            cnt+=1
        if not d.has_key(v2):
            d[v2]=cnt
            cnt+=1
        G[d[v1]].append(d[v2])
        GT[d[v2]].append(d[v1])

    n = len(d) # no of vertices

    return G, GT, n

def dfs(G, i, explored, s, leader, time, finish):
    """Performs a depth first search in graph G starting from vertex s
    Input: G - the input graph in the adjacency list representation via a dictionary
    i - the starting vertex
    explored - a set of explored vertices
    s - current source vertex for DFS
    leader - a dictionary that set the leader node for each node
    time - the current time, aka how many nodes we have processed
    finish - a dictionary that records the finishing time of each node"""
    
    explored.add(i) # add i to the set of explored vertices
    leader[i] = s[0] # set i's leader
    for j in G[i]: # for every edge (i, j)
        if j not in explored:
            dfs(G, j, explored, s, leader, time, finish)
    time[0] += 1 
    finish[i] = time[0]

def dfs_loop(G, n):
    """Performs and outputs a topological sort of graph G using dfs
    Input: G - the input graph in the adjacency list representation via a dictionary
    n - the largest vertex number"""

    explored = set() # a set of explored vertices
    finish = {i: 0 for i in range(1, n+1)} # a dictionary that records the finishing time of each node
    leader = {i: 0 for i in range(1, n+1)} # a dictionary that set the leader node for each node.
                                           # Nodes with the same leader node are in the same SCC 
    time = [0] # number of nodes processed so far
    s = [0] # current source vertex
    
    while n > 0:
        if n not in explored:
            s[0] = n
            dfs(G, n, explored, s, leader, time, finish)
        n -= 1
    return finish, leader

def makeFinishedTimeGraph(G, n, finish):
    """Constructs a graph based on the finishing time, specifically after the first dfs_loop on G's transpose
    Input: G - the input graph in the adjacency list representation via a dictionary
    n - the largest vertex number
    finish - a dictionary that records the finishing time of each node"""
    
    finishedGraph = {}
    for i in range(1, n+1):
        temp = []
        for x in G[i]:
            temp.append(finish[x])
        finishedGraph[finish[i]] = temp
    return finishedGraph
    
def main():
    # Make a graph and its transpose from the given data
    G, GT, n = make_graph()

    # benchmark the algorithm (which doesn't involve making the graph and outputting the final statistics)
    start = time.clock()
    
    # first loop using DFS over the transpose of G
    finishing_time, leader = dfs_loop(GT, n)

    # construct a new graph based on the finishing time of each node
    newGraph = makeFinishedTimeGraph(G, n, finishing_time)

    # second loop using DFS, this time over G
    finishing_time, leader = dfs_loop(newGraph, n)

    # stop the benchmark process
    elapsed = round(time.clock() - start, 3)
    
    # now process the SCC based on the nodes' finishing times
    lst = sorted(leader.values()) # sort the leaders
    final_stats = []
    start = 0 
    for i in range(n-1):
        if lst[i] != lst[i+1]:
            final_stats.append(i-start+1) # length of all the nodes with the same leader, i.e. in the same SCC
            start = i + 1 # the starting index of the next set of SCC components
    final_stats.append(n-start) # last SCC
    final_stats = sorted(final_stats) # sorted the final statistics in ascending order
    print("Number of Strongly Connected Components: ", len(final_stats))
    print("The algorithm took", elapsed, "seconds to finish")

if __name__ == '__main__':
    main()
