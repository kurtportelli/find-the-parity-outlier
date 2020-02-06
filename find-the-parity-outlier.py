def find_outlier(integers):
    odd_even = [n % 2 for n in integers]
    odd = odd_even.count(1)
    if odd == 1:
        return integers[odd_even.index(1)]
    else:
        return integers[odd_even.index(0)]
