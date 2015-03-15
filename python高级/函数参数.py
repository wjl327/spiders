def compute(fun, lst, initial):
    amount = initial
    for num in lst:
        amount = fun(amount, num)
    return amount

print compute(lambda x, y: x+y, range(5), 0)
print compute(lambda x, y: x-y, range(4), 10)
print compute(lambda x, y: x*y, [1,2,3,4,5], 1)
