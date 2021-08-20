"""
It's a widely used graph traversal algorithm.
It explores as far as possible along each branch
before backtracking.So it does not need pointers
unlike bfs.memory friendly.Time complexity of
traversing a graph with dfs is O(v+e).It has 
several applications:topological ordering of
kosaraju algorithm or detecting cycles.
"""
visited = []


def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.append(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


if __name__ == '__main__':
    graph = {
        '5': ['3', '7'],
        '3': ['2', '4'],
        '7': ['8'],
        '2': [],
        '4': ['8'],
        '8': []
    }
    dfs(visited, graph, '5')
