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
    S = input()
    count = 0
    b_count = 0

    for d in S[::-1]:
        tmp_b_count = (int(d) - count) % 10
        b_count += tmp_b_count
        count = (count + tmp_b_count) % 10
    
    print(len(S) + b_count)



    


    

if __name__ == '__main__':
    main()