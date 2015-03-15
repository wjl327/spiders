def pak(fun, lst):
    rst = []
    for item in lst:
        rst.append(fun(item))
    return rst

print pak(lambda x: x * 5, range(5))
