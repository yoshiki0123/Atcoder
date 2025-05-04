#library
import sys, re
from math import ceil, floor, sqrt, pi, gcd
from collections import deque, Counter
from bisect import bisect, bisect_left, bisect_right
from functools import lru_cache
from itertools import permutations, combinations

sys.setrecursionlimit(10**6)
INF = float('inf')

#def


#main
def main():
    N, K = map(int, input().split())
    MOD = 10**9

    A_list = [1] * K
    total = sum(A_list)

    for i in range(K, N+1):
        A_list.append(total % MOD)
        total += A_list[-1] - A_list[-K-1]

    if N < K:
        print(1)
    else:
        print(A_list[N] % MOD)


if __name__ == '__main__':
    main()