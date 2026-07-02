
def print_count_down(n :int):
    if n <= 0:
        return '   -> Done.'

    return f'{n}' + ' ' +  str(print_count_down(n-1))
#print(print_count_down(5))

def sum_odd_numbers(n :int):
    if n <= 0:
        return 0

    if n % 2 == 0:
        return sum_odd_numbers(n-1)

    return n + sum_odd_numbers(n-1)
#print(sum_odd_numbers(7))

def power(base :int, exponent :int):
    if exponent <= 0:
        return 1

    return base * power(base, exponent-1)
#print(power(6,3))

def max_in_list(lst :list,maximum=0):
    if len(lst) == 1:
        return lst[0] if lst[0] > maximum else maximum
    #print({"maximum":maximum,
    #       "list":lst})
    return max_in_list(lst[1:] ,maximum = lst[0] if lst[0]>maximum else maximum)
#print("max in list : ",max_in_list([0,0,0,0,2,0,2,3]))

def sum_even(lst:list):
    if len(lst) == 0:
        return 0

    if lst[0] % 2 == 1:
        return sum_even(lst[1:])

    return lst[0] + sum_even(lst[1:])
#print(sum_even([0,1,2,3,4]))

def sum_digits(n :int):
    if n <= 0:
        return 0
    return n%10 + sum_digits(n//10)
#print(sum_digits(3691))




