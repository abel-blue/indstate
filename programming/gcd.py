import math
import itertools

lis=[38, 75, 32, 62, 87, 52, 11, 29, 80, 15]
# lis =[25, 7, 30, 9]
for i in lis:
    for x in lis:
        if((i!=x)&(math.gcd(i,x)>1)):
            pair_order_list = itertools.permutations(lis, 2)
            list_of_tuples = list(pair_order_list)
            pairs = list_of_tuples
            unique = set(tuple(sorted(p)) for p in pairs)
print("total: ", sum(1 for a,b in unique if math.gcd(a,b)>1))