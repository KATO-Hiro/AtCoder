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
        vi = q.popleft()
        d = dist[vi]

        if vi * a < v_max and dist[vi * a] == inf:
            dist[vi * a] = d + 1
            q.append(vi * a)
        
        if vi >= 10 and vi % 10 != 0:
            vi_str = str(vi)
            vi_new = int(vi_str[-1] + vi_str[:-1])

            if dist[vi_new] == inf:
                dist[vi_new] = d + 1
                q.append(vi_new)
        
    ans = dist[n]

    if ans == inf:
        print(-1)
    else:
        print(ans)


if __name__ == "__main__":
    main()
