import ast
# x = eval("10+20+30")
# print(x)
#
#
# x = eval(input("Enter expression: "))
# print(x)
#
#
# l = eval(input("Enter list: "))
# print(type(l))
# print(l)

# a,b,c=[ast.literal_eval(x) for x in input("Enter 3 values: ").split()]
# print(type(a))
# print(type(b))
# print(type(c))

# split("x") → cuts the string wherever character x occurs
# separator is removed from the result

a,b,c=input("Enter 3 values: ").split("5")
print(a)
print(type(a))
print(type(b))
print(type(c))