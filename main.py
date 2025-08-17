class School_Method:
    def addition(a, b, B):
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
        