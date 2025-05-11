#library
import sys, re, heapq
from math import ceil, floor, sqrt, isqrt, pi, gcd, comb
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import permutations, combinations, product

sys.setrecursionlimit(10**6)
INF = float('inf')

#class

#def

#main
def main():
    H, W = map(int, input().split())
    grid = [list(input()) for _ in range(H)]

    ans = [['' for _ in range(W)] for _ in range(H)]
    dist = [[INF] * W for _ in range(H)]
    que = deque()

    for i in range(H):
        for j in range(W):
            if grid[i][j] == 'E':
                que.append((i, j))
                dist[i][j] = 0
                ans[i][j] = 'E'

    dirs = [(-1, 0, 'v'), (1, 0, '^'), (0, -1, '>'), (0, 1, '<')]

    while que:
        y, x = que.popleft()
        for dy, dx, arrow in dirs:
            ny, nx = y + dy, x + dx
            if 0 <= ny < H and 0 <= nx < W:
                if grid[ny][nx] == '.' and dist[ny][nx] > dist[y][x] + 1:
                    dist[ny][nx] = dist[y][x] + 1
                    ans[ny][nx] = arrow
                    que.append((ny, nx))

    for i in range(H):
        row = ''
        for j in range(W):
            if grid[i][j] == '#':
                row += '#'
            elif grid[i][j] == 'E':
                row += 'E'
            else:
                row += ans[i][j]
        print(row)

if __name__ == '__main__':
    main()