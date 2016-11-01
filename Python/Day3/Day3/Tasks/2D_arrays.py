students = [['Joe', 'Kim'], ['Sam', 'Sue'], ['Kelly', 'Chris']]
print(students)
print(students[0])
print(students[1])  # 2D array, these prints let you choose which row to print out, or a specific person to print out
print(students[2])
print(students[2][1])
import random

ROWS = 3
COLS = 4

students = [['Joe', 'Kim'], ['Sam', 'Sue'], ['Kelly', 'Chris']]

def column(matrix, i):
    return