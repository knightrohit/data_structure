""" Input: a = "11", b = "1"
    Output: "100"
"""

def add(a, b):
    a, b = int(a, 2), int(b, 2)
    if not a or not b:
        return a or b

    carry = 1
    while carry:
       sum_without_carry = a ^ b
       carry = (a & b) << 1
       a, b = sum_without_carry, carry

    return bin(sum_without_carry)[2:]

print(add('11', '1'))
