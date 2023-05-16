# EXERCISE 6:           Checksum
# Problem Statement:    Create function calc_checksum(digits) that performs
#                       a checksum of a number of any length given as a string
#                       with the n digits modeled as z1 to zn:
#                       z1 z2 z3...zn -> (1*z1+2*z2+3*z3+...+n*zn)%10
# Examples:
#
# Input		|	Sum		                                |	Result
#-----------|-------------------------------------------|-------------
#		    |	        				                |
# "11111"	| 1 + 2  + 3  + 4  + 5		                | 15 % 10 = 5
# "87654321"| 8 + 14 + 18 + 20 + 20 + 18 + 14 + 8 = 120 | 120 % 10 = 0

def calc_checksum(digits):
    if not digits.isdigit():
        raise ValueError("input error: it should all be digits")
    total_digits = len(digits)
    sum = 0

    for i in range(total_digits):
        sum += (i + 1)*(int(digits[i]))
    
    checksum = sum % 10

    return checksum

users_input = input("Enter a natural number: ")

result = calc_checksum(users_input)

print(f"Checksum result is {result}")
