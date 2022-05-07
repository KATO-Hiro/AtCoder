# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, m, q = map(int, input().split())
    wv = list()

    for i in range(n):
        wi, vi = map(int, input().split())
        wv.append((wi, vi))
    
    wv = sorted(wv)
    x = list(map(int, input().split()))

    # ナップザックDPと思いきや、貪欲法
    # 背理法で仮定(最適でない操作を行ったにも関わらず、貪欲法と同じ操作になる)の矛盾を示す
    for _ in range(q):
        li, ri  = map(int, input().split())
        li -= 1
        ri -= 1

        boxes = list()

        for i in range(m):
            if li <= i <= ri:
                continue

            boxes.append(x[i])
        
        used_items = [False] * n
        ans = 0

        for box in sorted(boxes):
            value, index = -1, -1

            for i in range(n):
                wi, vi = wv[i]

                if used_items[i]:
                    continue 

                if  wi > box:
                    continue

                if vi > value:
                    value = vi
                    index = i
            
            if index == -1:
                continue

            used_items[index] = True
            ans += wv[index][1]

        print(ans)


if __name__ == "__main__":
    main()
