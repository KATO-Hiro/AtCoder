# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    h, w = map(int, input().split())
    s = [list(input().rstrip()) for _ in range(h)]
    dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for i in range(h):
        for j in range(w):
            if s[i][j] == ".":
                continue

            count = 0

            for dx, dy in dxy:
                nx = j + dx
                ny = i + dy

                if nx < 0 or nx >= w or ny < 0 or ny >= h:
                    continue
                if s[ny][nx] == ".":
                    continue

                count += 1
            
            if count == 0:
                print("No")
                exit()
    
    print("Yes")


if __name__ == "__main__":
    main()
