# -*- coding: utf-8 -*-


def main():
    from collections import deque
    import sys

    input = sys.stdin.readline

    a, n = map(int, input().split())
    digit = len(list(str(n)))
    v_max = 10 ** digit
    inf = 10 ** 9
    dist = [inf] * v_max
    dist[1] = 0
    q = deque()
    q.append(1)

    while q:
        qi = q.popleft()
        di = dist[qi]
        new_qi = qi * a

        if new_qi < v_max and dist[new_qi] == inf:
            dist[new_qi] = di + 1
            q.append(new_qi)

        if qi >= 10 and qi % 10 != 0:
            tmp = list(str(qi))
            t = int("".join([tmp[-1]] + tmp[:-1]))

            if dist[t] == inf:
                dist[t] = di + 1
                q.append(t)
    
    if dist[n] == inf:
        print(-1)
    else:
        print(dist[n])


if __name__ == "__main__":
    main()
