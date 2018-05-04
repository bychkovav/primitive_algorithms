__author__ = 'Alexey'

import Solution as search
import math

#search_equal tests

arr = list(range(1000000))

res = search.search_not_equal(485000, arr)
assert res == arr.index(484999) or res == arr.index(485001)

res = search.search_not_equal(0, arr)
assert res == arr.index(0) or res == arr.index(1)

res = search.search_not_equal(999999, arr)
assert res == arr.index(999998) or res == arr.index(1000000)
#==================
