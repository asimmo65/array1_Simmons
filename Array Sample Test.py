#Given a number n, for each integer i in the range from
    # 1 to n inclusive, print one valueper line as follows
#if i is a multiple of both 3 and 5 print Fizzbuzz
#if i is a multiple of 3 (but not of 5), print Fizz
#if i is a multiple of 5 (but not of 3), print Buzz
#if i is not a multiple of 3 or 5 print the value of i
multiples_three = []

from array import*


array1 = int(input("enter number: "))
if( array1 % 3 == 0 and array1 % 5 == 0 ):
    print("Fizzbuzz")
    multiples_three.append(array1)
    print(multiples_three)

if( array1 % 3 == 0 and array1 % 5 > 0):
    print("Fizz")
    print(multiples_three)

if( array1 % 3 > 0 and array1 % 5 == 0):
    print("Buzz")
    print(multiples_three)

elif(array1 % 3 > 0 and array1 % 5 > 0):
    print(array1)
    print(multiples_three)