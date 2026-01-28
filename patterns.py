# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
#
#
# *****
#
# *****
#
# *****
#
# *****
#
# *****

def solidsquare(n):
    for i in range(n):
        for j in range(n):
            print("*",end="")
        print()

# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
#
# *
#
# **
#
# ***
#
# ****
#
# *****

def RightTriangleStar(n):
    for i in range(n):
        for j in range(0,i+1):
            print("*",end="")
        print()

# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
#
#
# 1
#
# 12
#
# 123
#
# 1234
#
# 12345

def rightanglecolumn(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end="")
        print()
# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
#
# 1
#
# 22
#
# 333
#
# 4444
#
# 55555

def rightanglerow(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(i,end="")
        print()

# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
#
# *****
#
# ****
#
# ***
#
# **
#
# *
def invertedrighttriangle(n):
    for i in range(n):
        for j in range(n-i):
            print("*",end="")
        print()

# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
#
# 12345
#
# 1234
#
# 123
#
# 12
#
# 1

def righttrianglenum(n):
    for i in range(n):
        for j in range(1,n-i+1):
            print(j,end="")
        print()

# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
#
#     *
#    ***
#   *****
#  *******
# *********

def starpyramid(n):
    for i in range(n):
        for j in range(2*n):
                if j < n - i - 1:
                    print(" ", end="")
                elif j>=n+i:
                    print(" ", end="")
                else:
                    print("*",end="")
        print()

# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
#
# *********
#  *******
#   *****
#    ***
#     *

# def invertedstarpyramid(n):
#     for i in range(n):
#         print(" "*i+"*"*(2*(n-i)-1))

def invertedstarpyramid(n):
    for i in range(n):
        for j in range(2*n):
            if j<i:
                print(" ",end="")
            elif j>=2*n-i-1:
                print(" ",end="")
            else:
                print("*",end="")
        print()

# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
#     *
#    ***
#   *****
#  *******
# *********
# *********
#  *******
#   *****
#    ***
#     *

def stardiamond(n):
    for i in range(n):
        print(" "*(n-i-1)+"*"*(2*i+1))
    for i in range(n):
        print(" "*i+"*"*(2*(n-i)-1))

# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
#
# *
#
# **
#
# ***
#
# ****
#
# *****
#
# ****
#
# ***
#
# **
#
# *

def rightaligneddiamond(n):
    for i in range(n):
        print("*"*(i+1))
    for i in range(n-1):
        print("*"*(n-i-1))

n=int(input())
solidsquare(n)
RightTriangleStar(n)
rightanglecolumn(n)
rightanglerow(n)
invertedrighttriangle(n)
righttrianglenum(n)
starpyramid(n)
print()
invertedstarpyramid(n)
print()
stardiamond(n)
rightaligneddiamond(n)
