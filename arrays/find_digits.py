# -> Given an integer, for each digit that makes up the integer determine whether it is a divisor. Count the number of divisors occurring within the integer.

n = 120

def findDigits(n):
    divisor_count = 0
    digits = [int(d) for d in str(n)] # convert the integer into list of numbers

    for i in range(len(digits)):
        if digits[i] == 0:
            continue
        
        if n % digits[i] == 0:
            divisor_count += 1

    return divisor_count 


print(findDigits(n))