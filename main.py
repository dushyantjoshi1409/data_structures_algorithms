#palindrome
lst = [1, 2, 3, 4, 5]#
first_index = 0
last_index = len(lst)-1
while first_index <= last_index:
    if lst[first_index] != lst[last_index]:
        print("Not a palindrome")
        break
    first_index += 1
    last_index -= 1
else:
    print("Palindrome")
