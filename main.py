import math
import sys

def school_method_addition(a, b, B):
    # convert the input integers to strings
    a_num = str(a)
    b_num = str(b)

    # find the length of the longer string
    max_length = max(len(a_num), len(b_num))

    # pad thr shorter string with zeros
    if len(a_num) < max_length:
        zeropad = '0' * (max_length - len(a_num))
        a_num = zeropad + a_num
    else:
        zeropad = '0' * (max_length - len(b_num))
        b_num = zeropad + b_num
    
    #initialise the result and carry strings
    result = []
    carry = 0

    # iterate through the strings from least significant to most signficiant digit (max -> 0)
    for i in range(max_length -1, -1, -1):
        add = int(a_num[i]) + int(b_num[i]) + carry # addition
        result.append(str(add % B)) # append the last digit of addition to result
        carry = int(add / B) # update the carry for the next iteration

    # if a carry is left over after last itersttion, append to result
    if carry > 0:
        result
        result.append(str(carry))

    # current string is in reverse order, so flip it
    result_add =''
    for digit in reversed(result):
        result_add += digit

    return result_add

def karatsuba_multiplication(a, b, B):

    if a < B or b < B: # base case of recursion
        return a * b

    # find the length of the longer number
    length = max(math.ceil(math.log(a + 1, B)), math.ceil(math.log(b + 1, B)))

    # calculate split point
    k = length // 2


    # Split a and b to let a = a1 * B^k + a0 and b = b1 * B^k + b0
    a1 = a // B**k
    a0 = a % B**k
    b1 = b // B**k
    b0 = b % B**k


    # recursively calculate p2, p1 and p0 following lecture 4 algorithm
    p2 = karatsuba_multiplication(a1, b1, B)
    p0 = karatsuba_multiplication(a0, b0, B)
    p1 = karatsuba_multiplication(a1 + a0, b1 + b0, B)

    # return result
    return (p2 * B**(2*k)) + ((p1 - (p2 + p0)) * B**k) + p0

def to_int(num, B):
    if num == 0:
        return "0"
    digits = []
    while num > 0:
        digits.append(str(num % B))
        num //= B
    return ''.join(reversed(digits))
        
# main file starts (read inputs, call functions, print result)
line = sys.stdin.readline().strip()
I1_str, I2_str, B_str = line.split()
B = int(B_str)

# Addition
addition_result = school_method_addition(I1_str, I2_str, B)

# Multiplication
karatsuba_int = karatsuba_multiplication(int(I1_str, B), int(I2_str, B), B)
karatsuba_result = to_int(karatsuba_int, B)

# Division (always 0)
div = "0"

# Print results
print(addition_result, karatsuba_result, div)