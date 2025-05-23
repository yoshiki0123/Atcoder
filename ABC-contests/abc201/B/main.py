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

#main
def main():
    N = int(input())
    mountains = []
    for _ in range(N):
        S, T = input().split()
        T = int(T)
        mountains.append([T, S])
    
    mountains.sort(reverse=True)
    print(mountains[1][1])

        

if __name__ == '__main__':
    main()