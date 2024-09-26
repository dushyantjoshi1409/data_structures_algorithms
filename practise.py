# def sum_(n):
#     a = 1
#     b = 1
#     if n == 1:
#         print(a)
#     else:
#         print(a)
#         print(b)
#         for i in range(2, n):
#             c = a+b
#             a = b
#             b = c
#             print(c, end=' ')
# sum_(5)

def fib(n):
    fib_list = [1, 1]
    for i in range(n):
        fib_list.append((fib_list[-1]+fib_list[-2]))
    print(fib_list)
fib(5)