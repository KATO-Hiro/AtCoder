# -*- coding: utf-8 -*-


def main():
    import sys

    input = sys.stdin.readline

    a, b, c, d = map(int, input().split())
    e = [list(map(int, input().split())) for _ in range(c)]
    ans = 0
    
    for score in range(0, 100 + 1):
        people_count = 0

        for ei in e:
            count = 0

            for eij in ei:
                if eij >= score:
                    count += 1
            
            if count >= b:
                people_count += 1
        
        if people_count >= d:
            ans = max(ans, score)
    
    print(ans)


if __name__ == "__main__":
    main()
