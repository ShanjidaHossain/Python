def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


#  Using user input
num1 = input("Enter 1st number: ")
num2 = input("Enter 2nd number: ")
num3 = input("Enter 3rd number: ")
max = max_num(num1, num2, num3)
print(max)


#  Using system input
max = max_num(89, 21, 18)
print(max)
max = max_num(6, 59, 18)
print(max)
