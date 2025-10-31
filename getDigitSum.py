"""
Digit sum calculator
what this means? let's take the number 573. the digit sum is 5 + 7 + 3, which is 15.

CALCULATING DIGIT SUM
For Python to read each individual digit of the number, we need to divide the number by ten, take the remainder and add to the sum. We then take the quotient of the division and repeat this process until the number is less than zero.

Let's use the number 570

while number > 0:
------------------------------------------------
digit_sum = 0
number = 570

Line 59 - ld = number % 10
570 % (MOD) 10 = 0 (remainder of 0)

Line 61 - digit_sum = digit_sum + ld
Adds 0 to the digit sum of 0

Line 63 - number = number // 10
570 // (DIV) 10 = 57 (quotient of the division is 57)
Update the number variable with the quotient
------------------------------------------------
digit_sum = 0
number = 57

Line 59 - ld = number % 10
57 % (MOD) 10 = 7 (remainder of 7)

Line 61 - digit_sum = digit_sum + ld
Adds 7 to the digit sum of 0

Line 63 - number = number // 10
57 // (DIV) 10 = 5 (quotient of the division is 5)
Update the number variable with the quotient
------------------------------------------------
digit_sum = 7
number = 5

Line 59 - ld = number % 10
5 % (MOD) 10 = 5 (remainder of 5)

Line 61 - digit_sum = digit_sum + ld
Adds 5 to the digit sum of 7

Line 63 - number = number // 10
5 // (DIV) 10 = 0 (quotient of the division is 5)
Update the number variable with the quotient
"""


def main():
    number = int(input("Enter a number to find the digit sum:\n"))
    digit_sum = 0

    while number > 0:
        # takes the remainder of the number when dividing by ten (to find the last digit)
        ld = number % 10
        # adds this digit to the sum
        digit_sum = digit_sum + ld
        # takes the quotient when the original number is divided by ten
        number = number // 10

    # prints the digit sum
    print(digit_sum)

# run the program

main()


