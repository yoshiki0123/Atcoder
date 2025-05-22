#library
import sys, re, heapq
from math import sin, cos, radians, ceil, floor, sqrt, isqrt, pi, gcd, comb
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import permutations, combinations, product

sys.setrecursionlimit(10**6)
INF = float('inf')

#class

#def
def n_minus_1_sum(n):
    return n*(n-1) // 2


#main
def main():
    N = int(input())
    A = list(map(int, input().split(' ')))

    mod = 200
    A = [a % 200 for a in A]
    counts = [0] * 200

    for e in A:
        counts[e] += 1
    
    ans = 0
    for count in counts:
        ans += n_minus_1_sum(count)
    
    print(ans)

if __name__ == '__main__':
    main()