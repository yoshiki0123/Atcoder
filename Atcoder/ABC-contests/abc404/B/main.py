#library
import sys, re
from math import ceil, floor, sqrt, isqrt, pi, gcd, comb
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import permutations, combinations, product

sys.setrecursionlimit(10**6)
INF = float('inf')

#class

#def
def rotate(grid):
    N = len(grid)
    return [[grid[N -1 -j][i] for j in range(N)] for i in range(N)]

def diff_count(grid1, grid2):
    N = len(grid1)
    diff_count = 0
    for i in range(N):
        for j in range(N):
            if grid1[i][j] != grid2[i][j]:
                diff_count += 1
    return diff_count

#main
def main():
    N = int(input())
    S = [list(input()) for _ in range(N)]
    T = [list(input()) for _ in range(N)]
    

    ans = INF
    for i in range(4):
        ops = diff_count(S, T) + i
        ans = min(ops, ans)
        S = rotate(S)

    print(ans)


if __name__ == '__main__':
    main()