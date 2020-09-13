'''
Problem Name: Largest and smallest value from the Addition
Author: Ayushi Rawat
Date: 13-09-2020
'''

def num_to_word(number):
  if number == 1 :
    return "one"
  if number == 2 :
    return "two"
  if number == 3 :
    return "three"
  if number == 4 :
    return "four"
  if number == 5 :
    return "five"
  if number == 6 :
    return "six"
  if number == 7 :
    return "seven"
  if number == 8 :
    return "eight"
  if number == 9 :
    return "nine"
  if number == 10 :
    return "ten"
  if number == 11 :
    return "eleven"
  if number == 12 :
    return "twelve"
  if number == 13 :
    return "thirteen"
  if number == 14 :
    return "fourteen"

  if number == 15 :
    return "quarter"
  
  if number == 16 :
    return "sixteen"
  if number == 17 :
    return "seventeen"
  if number == 18 :
    return "eighteen"
  if number == 19 :
    return "nineteen"
  if number == 20 :
    return "twenty"
  if number == 21 :
    return "twenty one"
  if number == 22 :
    return "twenty two"
  if number == 23 :
    return "twenty three"
  if number == 24 :
    return "twenty four"
  if number == 25 :
    return "twenty"
  if number == 26 :
    return "twenty six"
  if number == 27 :
    return "twenty seven"
  if number == 28 :
    return "twenty eight"
  if number == 29 :
    return "twenty nine"

  if number == 30 :
    return "half"




data = list(map(int ,input().split()))

prefix = ""
suffix = ""

# cases

#1 data[1] == 0
if data[1] == 0 :

  suffix = " o' clock "
  prefix = num_to_word(data[0])

#2 data[1] <= 30
if data[1] <= 30 and data[1] > 0 :
  if data[1] == 1:
    prefix = num_to_word(data[1]) + " minute past "
    suffix = num_to_word(data[0])
  elif data[1] == 15 or data[1] == 30:
    prefix = num_to_word(data[1]) + " past "
    suffix = num_to_word(data[0])
  
  else:
    prefix = num_to_word(data[1]) + " minutes past "
    suffix = num_to_word(data[0])

#2 data[1] > 30

if data[1] > 30 :
  if 60 - data[1] == 1:

    prefix = num_to_word(60 - data[1]) + " minute to "
    suffix = num_to_word(data[0] + 1)
  elif 60 - data[1] == 15 or 60 - data[1] == 30:
    prefix = num_to_word(60 - data[1]) + " to "
    suffix = num_to_word(data[0] + 1)
  else:
    prefix = num_to_word(60 - data[1]) + " minutes to "
    suffix = num_to_word(data[0] + 1)


print(prefix + suffix)