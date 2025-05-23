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
    A = list(map(int, input().split(' ')))
    A = sorted(A)

    if A[2] - A[1] == A[1] - A[0]:
        print('Yes')
    else:
        print('No')
    

if __name__ == '__main__':
    main()