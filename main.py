import math
import sys

def school_method_add(a, b, B):
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

def school_method_mult(a, b, B):
    # 0 base case
    if a == "0" or b == "0":
        return "0"

    # singular digit base case
    if len(a) == 1 and len(b) == 1:
        return str(int(a, B) * int(b, B))

    n = max(len(a), len(b)) # check which number is longer
    k = n // 2 # set the split point

    # zero pad the shorter number
    a = a.zfill(n)
    b = b.zfill(n)

    # split the numbers into lower and upper parts
    a1, a0 = a[:-k], a[-k:]
    b1, b0 = b[:-k], b[-k:]

    # recursively call for each part of equation as given by lecture notes
    p2 = school_method_mult(a1, b1, B)
    p0 = school_method_mult(a0, b0, B)
    p1 = school_method_mult(school_method_add(a1, a0, B), school_method_add(b1, b0, B), B)

    # combine the results using school method addition and subtraction
    mult1 = p2 + "0" * (2 * k)
    mult2 = school_method_sub(p1, school_method_add(p2, p0, B), B) + "0" * k
    result = school_method_add(school_method_add(mult1, mult2, B), p0, B)

    return result.lstrip("0") or "0"


def school_method_sub(a, b, B):
    # for school method, we have to assume a >=b
    a = [int(d) for d in a[::-1]]
    b = [int(d) for d in b[::-1]]
    
    # make empty list for result and initialise borrow
    result = []
    borrow = 0

    # iterate through strings a and b
    for i in range(len(a)):
        ai = a[i]
        if i < len(b):
            bi = b[i]
        else: 
            bi = 0
        diff = ai - bi - borrow # subtract the columns
        if diff < 0: # if subtraction is negative, we need to borrow
            diff += B
            borrow = 1
        else: # no borrow needed
            borrow = 0
        result.append(diff)
    
    # Remove any leading zeros
    while len(result) > 1 and result[-1] == 0:
        result.pop()
    
    return ''.join(str(d) for d in result[::-1])

def strip_leading_zeros(s: str) -> str:
    return s.lstrip("0") or "0" # return 0 if string is empty


def karatsuba_multiplication(a, b, B):
    # remove any leading zeros
    a = strip_leading_zeros(a)
    b = strip_leading_zeros(b)

    # base case: 1-digit multiplication
    if len(a) == 1 or len(b) == 1:
        return school_method_mult(a, b, B)

    # zero pad to equal lengths
    n = max(len(a), len(b))
    if n % 2 == 1:
        n += 1
    a = a.zfill(n)
    b = b.zfill(n)
    m = n // 2 # set the split point

    # split for each number (coefficient)
    a1, a0 = a[:-m], a[-m:]
    b1, b0 = b[:-m], b[-m:]

    # recursive calls to karatsuba multiplication and calls to school method addition and subtraction
    p2 = karatsuba_multiplication(a1, b1, B)
    p0 = karatsuba_multiplication(a0, b0, B)
    sum_a = school_method_add(a1, a0, B)
    sum_b = school_method_add(b1, b0, B)
    p1 = karatsuba_multiplication(sum_a, sum_b, B)

    # (p1 - p2 - p0)
    temp = school_method_sub(p1, p2, B)
    middle = school_method_sub(temp, p0, B) 

    # shift the terms
    p2_shifted = p2 + "0" * (2*m) # shift p2 by 2*m
    middle_shifted = middle + "0" * m # shift middle by m

    # final addition
    result = school_method_add(school_method_add(p2_shifted, middle_shifted, B), p0, B)
    return strip_leading_zeros(result)

        
# main file starts (read inputs, call functions, print result)
line = sys.stdin.readline().strip()
I1_str, I2_str, B_str = line.split()
B = int(B_str)

# Addition
addition_result = school_method_add(I1_str, I2_str, B)

# Multiplication
karatsuba_result = karatsuba_multiplication(I1_str, I2_str, B)

# Division (always 0)
div = "0"

# Print results
print(addition_result, karatsuba_result, div)