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
    N, M = map(int,input().split())
    recipes = [None] # indexを1から
    ingredient_to_recipes =  [[] for _ in range(N+1)]
    ingredient_to_recipes[0] = None
    bad_count = [None]

    for i in range(1, M+1):
        row = list(map(int, input().split(' ')))
        K = row[0]
        ingredients = [A for A in row[1:]]
        recipes.append(ingredients)
        bad_count.append(K)

        for ingredient in ingredients:
            ingredient_to_recipes[ingredient].append(i)
    
    B_list = list(map(int, input().split(' ')))
    ans = 0

    for B in B_list:
        for recipe_index in ingredient_to_recipes[B]:
            bad_count[recipe_index] -= 1
            if bad_count[recipe_index] == 0:
                ans += 1

        print(ans)
        
if __name__ == '__main__':
    main()