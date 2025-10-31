# getDigitSum

## Digit Sum? What's that?
What this means? Let's take the number 573. The digit sum is `5 + 7 + 3 = 15`.

## Okay...and how do we calculate this in Python?
In Python, we need to read each individual digit of the number to calculate the digit sum:

- Divide the number by ten, take the remainder (`% 10`) and add it to `digit_sum`.
- Take the quotient (`// 10`) and update the original number.
- Repeat until the original number is 0.

## ...a more detailed explanation?
Let's use the number `570`.

### `while number > 0:`

`digit_sum = 0`  
`number = 570`

### Line 59

`ld = number % 10`  
`570 % 10 = 0` (remainder of 0)

### Line 61

`digit_sum = digit_sum + ld`  
Adds 0 to the digit sum of 0 → `digit_sum = 0`

### Line 63

`number = number // 10`  
`570 // 10 = 57` (quotient of the division)  
Update the number variable → `number = 57`

---

`digit_sum = 0`  
`number = 57`

### Line 59

`ld = number % 10`  
`57 % 10 = 7` (remainder of 7)

### Line 61

`digit_sum = digit_sum + ld`  
Adds 7 → `digit_sum = 7`

### Line 63

`number = number // 10`  
`57 // 10 = 5` (quotient of the division)  
Update the number variable → `number = 5`

---

`digit_sum = 7`  
`number = 5`

### Line 59

`ld = number % 10`  
`5 % 10 = 5` (remainder of 5)

### Line 61

`digit_sum = digit_sum + ld`  
Adds 5 → `digit_sum = 12`

### Line 63

`number = number // 10`  
`5 // 10 = 0` (quotient of the division)  
Update the number variable → `number = 0`

---

Please take a look at the Python file for more detailed information!
