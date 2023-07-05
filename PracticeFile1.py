def even(n):
    if n % 2 != 0:
        return n
num = [23, 34,8,9,2,4,10]
even = list(filter(even, num))
print(even)


#or

num = [12,1,1,98, 8,2,17,20]
double = list(map(lambda n : n*2, num))
print(double)
#or

from functools import reduce
num = [12,1,1,98, 8,2,17,20]
sum = reduce(lambda a,b : a+b, num)
print(sum)