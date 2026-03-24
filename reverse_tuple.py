def reverse_tuple(t):
    return t[::-1]

# user input (space separated numbers)
t = tuple(map(int, input("Enter elements: ").split()))

print("Reversed tuple:", reverse_tuple(t))