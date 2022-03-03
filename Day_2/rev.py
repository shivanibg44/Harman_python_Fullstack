num = 5908
rn = 0
while num != 0:
    rem = num % 10
    rn = rn * 10 + rem
    num //= 10
print("Reversed Number: " + str(rn))