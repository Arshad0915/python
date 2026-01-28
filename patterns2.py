# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
#
# 1
#
# 0 1
#
# 1 0 1
#
# 0 1 0 1
#
# 1 0 1 0 1

def binarytriangle(n):
    for i in range(n):
        a=True if i%2==0 else False
        for j in range(i+1):
            print(int(a),end="")
            a=not a
        print()

# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
#
# 1        1
# 12      21
# 123    321
# 1234  4321
# 1234554321

def palindromic_num_pyramid(n):
    for i in range(1,n+1):
        for j in range(1,2*n+1):
            if j<=i:
                print(j,end="")
            elif j<2*n-i+1:
                print(" ",end="")
            else:
                print(2*n-j+1,end="")
        print()

# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
#
# 1
#
# 2 3
#
# 4 5 6
#
# 7 8 9 10
#
# 11 12 13 14 15

def floyd_triangle(n):
    num=1
    for i in range(n):
        for j in range(0,i+1):
            print(num,end=" ")
            num+=1
        print()


# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
#
# A
#
# AB
#
# ABC
#
# ABCD
#
# ABCDE

def alphabet_triangle(n):
    for i in range(n):
        num=65
        for j in range(0,i+1):
            print(chr(num),end="")
            num+=1
        print()

# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
#
# ABCDE
#
# ABCD
#
# ABC
#
# AB
#
# A
def inverted_alphabet_triangle(n):
    for i in range(n):
        num=65
        for j in range(n-i):
            print(chr(num),end="")
            num+=1
        print()

# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
#
# A
#
# BB
#
# CCC
#
# DDDD
#
# EEEEE

def same_letter_triangle(n):
    num=65
    for i in range(n):
        for j in range(0,i+1):
            print(chr(num),end="")
        num+=1
        print()


# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
#
#     A
#    ABA
#   ABCBA
#  ABCDCBA
# ABCDEDCBA

# def symmetric_alphabet_pyramid(n):
#     for i in range(n):
#         num=65
#         flag=True
#         for j in range(2*n-1):
#             if j<n-i-1:
#                 print(" ",end="")
#             elif j>n+i-1:
#                 print(" ",end="")
#             elif j<=n-1:
#                 print(chr(num), end="")
#                 num += 1
#             else:
#                 if flag:
#                     num-=2
#                     flag=False
#                 else:
#                     num-=1
#                 print(chr(num), end="")
#
#         print()
def symmetric_alphabet_pyramid(n):
    for i in range(n):
        for s in range(n - i - 1):
            print(" ", end="")
        ch = 65
        for j in range(i + 1):
            print(chr(ch), end="")
            ch += 1
        ch -= 2
        for j in range(i):
            print(chr(ch), end="")
            ch -= 1

        print()

# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
#
# E
#
# D E
#
# C D E
#
# B C D E
#
# A B C D E
def reverse_alphabet_triangle(n):

    for i in range(n):
        num=64+n-i
        for j in range(0,i+1):
            print(chr(num),end="")
            num+=1
        print()

# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
#
# **********
# ****  ****
# ***    ***
# **      **
# *        *
# *        *
# **      **
# ***    ***
# ****  ****
# **********
def inverted_hour_glass(n):
    for i in range(n):
        print("*"*(n-i)+" "*(2*i)+"*"*(n-i))
    for i in range(n):
        print("*"*(i+1)+" "*(2*n-(2*(i+1)))+"*"*(i+1))

# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
#
# *        *
# **      **
# ***    ***
# ****  ****
# **********
# ****  ****
# ***    ***
# **      **
# *        *

def butterfly(n):
    for i in range(n):
        print("*"*(i+1)+" "*(2*n-(2*(i+1)))+"*"*(i+1))
    for i in range(n):
        print("*"*(n-i-1)+" "*(2*(i+1))+"*"*(n-i-1))


# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
#
# *****
# *   *
# *   *
# *   *
# *****
def hollow_square(n):
    print("*"*n)
    for i in range(n-2):
        print("*"+" "*(n-2)+"*")
    print("*"*n)


# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
#
# 5 5 5 5 5 5 5 5 5
# 5 4 4 4 4 4 4 4 5
# 5 4 3 3 3 3 3 4 5
# 5 4 3 2 2 2 3 4 5
# 5 4 3 2 1 2 3 4 5
# 5 4 3 2 2 2 3 4 5
# 5 4 3 3 3 3 3 4 5
# 5 4 4 4 4 4 4 4 5
# 5 5 5 5 5 5 5 5 5
def concentric_num_square(n):
    for i in range(2*n):
        for j in range(2*n):
            top=i
            bottom=2*n-2-i
            left=j
            right=2*n-2-j
            print(n-min(top,left,right,bottom),end="")
        print()

n=int(input())
binarytriangle(n)
palindromic_num_pyramid(n)
floyd_triangle(n)
alphabet_triangle(n)
inverted_alphabet_triangle(n)
same_letter_triangle(n)
symmetric_alphabet_pyramid(n)
reverse_alphabet_triangle(n)
inverted_hour_glass(n)
print()
butterfly(n)
hollow_square(n)
concentric_num_square(n)