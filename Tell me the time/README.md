Tell me the time
==========================

## Problem Statement:
Given the time in numerals we may convert it into words, as shown below:
- 6:00 → six o’ clock
- 6:01 → one minute past six
- 6:10 → ten minutes past six
- 6:15 → quarter past six
- 6:28 → twenty eight minutes past six
- 6:30 → half past six
- 6.40 → twenty minutes to seven
- 6:45 → quarter to seven
- 6:47 → thirteen minutes to seven

At minutes = 0, use o’ clock. For 1 <= minutes <= 30, use past, and for 30 < minutes use to. Note the space between the apostrophe and clock in o’ clock. Write a program which prints the time in words for the input given in the format described.


## Example
```
Input: 5 47
A single line contains hours and minutes. Both are separated by a space. example: 7 13

Output: thirteen minutes to six
Print the time in words as described.

```

## Constraints
```
1 <= h <= 12
0 <= m <= 60
```

## Note:
```
You may assume that the secret number and your friend's guess only contain digits, and their lengths are always equal.
```