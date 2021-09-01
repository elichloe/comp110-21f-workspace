"""A program to practice numeric operators."""

__author__ = "730393169"


left: str = input("left hand: ") 

right: str = input("right hand: ") 

left_n = int(left)

right_n = int(right)


print(left + " ** " + right + " is " + str(left_n ** right_n))

print(left + " / " + right + " is " + str(left_n / right_n))


print(left + " // " + right + " is " + str(left_n // right_n))

print(left + " % " + right + " is " + str(left_n % right_n))