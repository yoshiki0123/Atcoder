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
    N = int(input())
    A = list(map(int, input().split(' ')))
    S = sum(A)
    ans = 0

    for i in range(N-1):
        S -= A[N-1-i]
        ans += A[N-1-i] * S
    
    print(ans)


    

if __name__ == '__main__':
    main()