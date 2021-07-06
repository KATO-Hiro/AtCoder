# -*- coding: utf-8 -*-


inf = 10 ** 12


def warshall_floyd(dist):
    '''
        Args:
            Distance matrix between two points.
        Returns:
            Matrix of shortest distance.
        Landau notation: O(n ** 3).
    '''

    v_count = len(dist[0])
    ans = 0

    for k in range(v_count):
        for i in range(v_count):
            for j in range(v_count):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
                
                if dist[i][j] != inf:
                    ans += dist[i][j]

    return ans



def main():
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    graph = [[inf for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if i == j:
                graph[i][j] = 0
    
    for _ in range(m):
        ai, bi, ci = map(int, input().split())
        ai -= 1
        bi -= 1
    
        graph[ai][bi] = ci
    
    print(warshall_floyd(graph))

if __name__ == "__main__":
    main()
