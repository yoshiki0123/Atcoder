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
    N, M, Q = map(int, input().split())
    user_admin = [set() for _ in range(N)]  
    full_admin = [False] * N  

    for _ in range(Q):
        query = list(map(int, input().split()))

        if query[0] == 1:
            X = query[1] - 1
            Y = query[2] - 1
            user_admin[X].add(Y)

        elif query[0] == 2:
            X = query[1] - 1
            full_admin[X] = True

        elif query[0] == 3:
            X = query[1] - 1
            Y = query[2] - 1
            if full_admin[X] or Y in user_admin[X]:
                print('Yes')
            else:
                print('No')

if __name__ == '__main__':
    main()