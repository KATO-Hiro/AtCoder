# -*- coding: utf-8 -*-


def main():
    from collections import deque
    import sys

    input = sys.stdin.readline

    a, n = map(int, input().split())
    digit = len(str(n))
    v_max = 10 ** digit
    inf = 10 ** 8
    dist = [inf] * v_max
    dist[1] = 0
    q = deque()
    q.append(1)

    while q:
        qi = q.popleft()
        di = dist[qi]

        if qi * a < v_max and dist[qi * a] == inf:
            dist[qi * a] = di + 1
            q.append(qi * a)

        if qi >= 10 and qi % 10 != 0:
            s = list(str(qi))
            t = int(''.join(map(str, [s[-1]] + s[:-1])))

            if dist[t] == inf:
                dist[t] = di + 1
                q.append(t)
    
    if dist[n] == inf:
        print(-1)
    else:
        print(dist[n])


if __name__ == "__main__":
    main()
