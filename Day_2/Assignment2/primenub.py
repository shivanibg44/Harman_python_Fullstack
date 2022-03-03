num1 = 2
num2 = 500
print("The Prime Numbers in the range are: ")
for num3 in range(num1, num2 + 1):
    if num3 > 1:
        for i in range(2, num3):
            if (num3 % i) == 0:
                break
        else:
            print(num3)