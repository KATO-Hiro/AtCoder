# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    n, x, y = map(int, input().split())

    def dfs(level, is_red):
        if level == 1:
            if is_red:
                return 0
            else:
                return 1
        
        if is_red:
            return dfs(level - 1, True) + dfs(level, False) * x
        else:
            return dfs(level - 1, True) + dfs(level - 1, False) * y
    
    print(dfs(n, True))


if __name__ == "__main__":
    main()
