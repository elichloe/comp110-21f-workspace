""" A program for relational operations."""
__author__ = "730393169"

left: str = input("Left-hand side: ")

right: str = input("Right-hand side:")

left_n = int(left)
right_n = int(right)

print(left + " < " + right + " is " + str(left_n < right_n))

print(left + " >= " + right + " is " + str(left_n >= right_n))

print(left + " == " + right + " is " + str(left_n == right_n))

print(left + " != " + right + " is " + str(left_n != right_n))