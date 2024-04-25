# Write a Python program to create a list by concatenating a given list with a range from 1 to n.
# my_list=['p','q']
# n=int(input())
# my_for=['{}{}'.format(j,i) for i in range(1,n+1) for j in my_list]
# print(my_for)
my_list=input().split()
n=int(input())
m=[]
for i in range(1,n+1):
    for j in my_list:
        m.append(f"{j}{i}")
print(m)