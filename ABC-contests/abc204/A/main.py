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
    x, y = map(int,input().split())
    s = {0, 1, 2}
    if x == y:
        print(x)
    else:
        s.remove(x)
        s.remove(y)
        print(*s)
    
    

if __name__ == '__main__':
    main()