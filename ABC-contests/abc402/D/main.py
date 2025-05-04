#library
import sys, re
from math import ceil, floor, sqrt, isqrt, pi, gcd, comb
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')

#def

#main
def main():
    N, M = map(int,input().split())

    parallels = N * [0]
    for _ in range(M):
        A, B = map(int,input().split())
        parallels[(A+B)%N] += 1

    ans = comb(M, 2)
    for count in parallels:
        ans -= comb(count, 2)

    print(ans)

if __name__ == '__main__':
    main()