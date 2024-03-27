# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    # Convert to binary
    bin_representation = bin(n)

    # Convert to string
    binary_str = str(bin_representation)
    binary_str_removing_prefix = binary_str[2:]

    # Create a 32 bits number
    total_length = 32
    binary_str_length = len(binary_str_removing_prefix)
    remaining_length = total_length - binary_str_length
    binary_str_32_bits = remaining_length * '0' + binary_str_removing_prefix

    # Replace 0s with 1s and 1s with 0s
    switched_str = ''.join(['1' if digit == '0' else '0' for digit in binary_str_32_bits])

    # Return decimal
    return int(switched_str, 2)


flipped_number = flippingBits(9)
print(flipped_number)

flipped_number = flippingBits(1)
print(flipped_number)
