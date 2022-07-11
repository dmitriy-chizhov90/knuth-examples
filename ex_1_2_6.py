import itertools
import math

# 3.
# Count of combinations from n by k.
def combi_count1(n, k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))

#def combi_count2(n, k):
#    return sum(1 for _ in itertools.combinations(range(n), k))

def check_combi_count(n, k, expected):
    r = combi_count1(n, k)
    print('combi count from {} by {} = {}, {}'.format(n, k, r, "OK" if r == expected else "!!! expected {}".format(expected)))

check_combi_count(52, 13, 635013559600)
check_combi_count(52, 51, 52)
check_combi_count(0, 0, 1)

