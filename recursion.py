#recursion_Practice

# def printnum(num):
#     if num == 1:
#         return 1
#     else:
#         return num + printnum(num - 1)
# print(printnum(5))

# num = 123
# count = 0
# while num > 0:
#     num //= 10
#     count += 1
# print(count) # now convert this to recursive way

# def count(num):
#     if num == 0:
#         return 1
#     elif(num>=1 and num<=9):
#         return 1
#     else:
#         return 1 + count(num // 10)
# print(count(1))

# # sum of digits using recursion
# def sum_of_digits(n):
#     if n == 0:
#         return 0
#     else:
#         return n % 10 + sum_of_digits(n // 10)

# print(sum_of_digits(12345))

#fibonicci_series
def fibonic_series(num):
    
    if num == 0:
        return 1
    if num == 1:
        return 1
    last = fibonic_series(num-1)
    second_last = fibonic_series(num-2)
    ans = last + second_last 
    return ans
print(fibonic_series(4))
        