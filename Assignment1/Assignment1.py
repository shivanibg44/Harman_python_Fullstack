num_input = input("Enter the input ")

try:
    int(num_input)
    it_is = True
except ValueError:
    it_is = False

print(it_is)