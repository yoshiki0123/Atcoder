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
    N = int(input())
    A = list(map(int, input().split(' ')))
    ans = 0
    for i in range(1, N+1):
        if i % 2 != 0:
            ans += A[i-1]

    print(ans)
    

if __name__ == '__main__':
    main()