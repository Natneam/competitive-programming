def one_in_bits(n:int) -> int:
    ones = 0
    while n !=0 :
        ones = ones +  (n & 1)
        n = n >> 1
    return ones

print(one_in_bits(1000))


# NOTES
# -----
# Be very comfortable with the bitwise operators, particularly XOR.
# Understand how to use masks and create them in an machine independent way,
# Know fast ways to clear the lowermost set bit (and by extension, set the lowermost 0, get its index, etc.)
# Understand signedness and its implications to shifting.
# Consider using a cache to accelerate operations by using it to brute-force small inputs.
# Be aware that commutativity and associativity can be used to perform operations in parallel and reorder operations.

# ~0, and negative representing negative binary number in python