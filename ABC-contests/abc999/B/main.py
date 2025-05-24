#library
import sys, re, heapq
from math import sin, cos, radians, ceil, floor, sqrt, isqrt, pi, gcd, comb
from collections import deque, Counter, defaultdict
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import permutations, combinations, product

sys.setrecursionlimit(10**6)
INF = float('inf')

#class

#def

#main
def main():
    X, Y = map(int,input().split())

    ans = 0
    for i in range(1, 7):
        for j in range(1, 7):
            if i + j >= X or abs(i - j) >= Y:
                ans += 1

    print(ans / 36)
    

if __name__ == '__main__':
    main()