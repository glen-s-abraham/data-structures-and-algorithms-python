"""
We visit every every vertex exactly once.
we visit each neighbour vertex then the neighbours of these
new vertices.Running time of the algorithm:O(v+e)
It has to stre a lot of pointers so it's not as efficient as
depth first search.It constructs shortest paths tree:Dijikstras
shortest path algorithm does a BFS if all the edge weight are
equal to 1.In AI and ML it can be proven to be very important
robots can discover the surroundings more easily with bfs than
dfs.It is also very important in maximum flow:the Edmonds-Karp
maximum flow algorithm uses BFS for finding augmenting pointes.
Cheyen's algorithm in garbage collection:Similar to mark and
sweep gs procedure, it helps to maintain the active references.
it uses bfs to detect all the references on the heap memory.
"""


def bfs(visited, graph, node):
    queue = []
    visited.append(node)
    queue.append(node)
    while queue:
        m = queue.pop(0)
        print(m)
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


if __name__ == '__main__':
    graph = {
        '5': ['3', '7'],
        '3': ['2', '4'],
        '7': ['8'],
        '2': [],
        '4': ['8'],
        '8': []
    }
    visited = []
    bfs(visited, graph, '5')
