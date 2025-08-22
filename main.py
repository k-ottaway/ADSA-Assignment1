import sys

def school_method_add(a, b, B):
    # get lengths of strings a and b
    i = len(a) - 1
    j = len(b) - 1

    # initialise carry and result
    carry = 0
    add_result = []

    # Loop through digits from right to left
    while i >= 0 or j >= 0 or carry:
        if i >= 0:
            digit_a = a[i]  
        else:
            digit_a = 0
        if j >= 0:
            digit_b = b[j]
        else:
            digit_b =0

        s = digit_a + digit_b + carry # sum of the digits and carry
        add_result.append(s % B) # append last digit of sum
        carry = s // B # update carry
        i -= 1 # decrement i and j
        j -= 1

    add_result.reverse() # reverse the result for correct order
    return add_result


def school_method_mult(a, b, B):
    # 0 base case
    if a == [0] or b == [0]:
        return [0]

    # Find maximum length of result
    len_a = len(a)
    len_b = len(b)
    mult_result = [0] * (len_a + len_b)  # result can be at most len_a + len_b digits long

    # Multiplication using school method
    for i in range(len_a - 1, -1, -1):
        carry = 0
        for j in range(len_b - 1, -1, -1):
            sum = mult_result[i + j + 1] + a[i] * b[j] + carry # holds sum before splitting
            mult_result[i + j + 1] = sum % B # stores last digit
            carry = sum // B  # remainder becomes a carry
        mult_result[i] += carry  # remaining carry goes to the next column
    return strip_leading_zeros(mult_result)


def school_method_sub(a, b, B):
    i = len(a) - 1  # last element in a
    j = len(b) - 1  # last element in b

    # initialise borrow and result
    borrow = 0
    sub_result = []
    
    while i >= 0:   # loops until all digits in a are processed
        digit_a = a[i] - borrow # get digit from a, subtract borrow
        if j >= 0:
            digit_b = b[j]
        else:   
            digit_b = 0

        if digit_a < digit_b:   # check if we need to borrow from future column
            digit_a += B
            borrow = 1
        else:
            borrow = 0

        sub_result.append(digit_a - digit_b)
        i -= 1
        j -= 1
    sub_result.reverse() # reverse the result for correct order
    return strip_leading_zeros(sub_result)


def strip_leading_zeros(input_list):
    i = 0
    while i < len(input_list) - 1 and input_list[i] == 0:  # skip leading zeros
        i += 1
    return input_list[i:]


def karatsuba_multiplication(a, b, B):
    a = strip_leading_zeros(a)
    b = strip_leading_zeros(b)

    if a == [0] or b == [0]: 
        return [0] # return 0 if a or b is 0

    n = max(len(a), len(b))
    if n < 4: # karatsuba "base case"
        return school_method_mult(a, b, B)
    
    # check that length is even
    if n % 2: 
        n += 1
    
    # zero pad a and b
    a = [0]*(n-len(a)) + a
    b = [0]*(n-len(b)) + b
    
    # Split the numbers
    k = n // 2
    a1, a0 = a[:k], a[k:]
    b1, b0 = b[:k], b[k:]

    # Solve subproblems as given by the lecture slides
    P0 = karatsuba_multiplication(a0, b0, B)
    P2 = karatsuba_multiplication(a1, b1, B)
    P1 = karatsuba_multiplication(school_method_add(a0, a1, B), school_method_add(b0, b1, B), B)
    mid = school_method_sub(school_method_sub(P1, P2, B), P0, B)

    P2_shifted = P2 + [0] * (2 * k)
    mid_shifted = mid + [0] * k

    # Combine the results
    kara_result = school_method_add(school_method_add(P2_shifted, mid_shifted, B), P0, B)
    return strip_leading_zeros(kara_result)

        
# main file starts (read inputs, call functions, print result)
input = sys.stdin.readline().strip() # read input
sa, sb, sB = input.split()  # split input into a, b and base B
B = int(sB) # converts string into an integer
  
a = [int(c) for c in sa.strip()] # converts a into list of digits
b = [int(c) for c in sb.strip()] # converts b into list of digits

addition = school_method_add(a, b, B) 
multiplication = karatsuba_multiplication(a, b, B) 
division = [0]  

# Converts results back into strings
addition_str = ''.join(str(d) for d in strip_leading_zeros(addition))   #removes any leading zeros
multiplication_str = ''.join(str(d) for d in strip_leading_zeros(multiplication))
division_str = '0'  

print(addition_str, multiplication_str, division_str)   # prints results