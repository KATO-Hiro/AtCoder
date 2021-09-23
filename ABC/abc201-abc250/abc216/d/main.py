# -*- coding: utf-8 -*-


def main():
    from collections import deque
    import sys

    input = sys.stdin.readline

    n, m = map(int, input().split())
    tubes = list()
    q = deque()

    for i in range(m):
        _ = int(input())
        a = deque(list(map(int, input().split())))
        q.append((a.popleft(), i)) # 先頭の値だけを全体を管理するキューに追加

        tubes.append(a)

    d = dict()

    while q:
        number, id = q.popleft()

        if number in d.keys():
            d[number].append(id)
        else:
            d[number] = [id]
        
        if len(d[number]) == 2:
            for i in d[number]:
                if len(tubes[i]) > 0:
                    q.append((tubes[i].popleft(), i))

            del d[number]

    if len(d.keys()) == 0:
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    main()
