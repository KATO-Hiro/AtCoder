# -*- coding: utf-8 -*-


def main():
    from collections import defaultdict, deque
    import sys

    input = sys.stdin.readline

    s = input().rstrip()
    n = len(s)
    t = "atcoder"
    graph = [[] for _ in range(n)]
    pieces = ""
    
    for si in s:
        pieces += str(t.index(si))
    
    for f, s in zip(pieces, pieces[1:]):
        ai = int(f)
        bi = int(s)

        graph[ai].append(bi)
        graph[bi].append(ai)
    
    goal = '0123456'
    dist = defaultdict(int)
    dist[pieces] = 0
    q = deque()
    q.append(pieces)

    while q:
        qi = q.popleft()
        di = dist[qi]

        for i in range(n):
            for to in graph[i]:
                tmp = list(qi)
                tmp[i], tmp[to] = tmp[to], tmp[i]
                tmp = ''.join(tmp)

                if tmp not in dist.keys():
                    dist[tmp] = di + 1
                    q.append(tmp)
    
    print(dist[goal])


if __name__ == "__main__":
    main()
