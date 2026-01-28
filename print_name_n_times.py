def print_n_times(name,n):
    if n<1:
        return
    print(name)
    print_n_times(name,n-1)

s=input()
n=int(input())
print_n_times(s,n)
