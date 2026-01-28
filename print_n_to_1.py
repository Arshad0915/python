def print_n_1(n):
    if n<1:
        return
    print(n)
    print_n_1(n-1)

n=int(input())
print_n_1(n)
