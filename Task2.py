#Write a Python program to find common items in two lists.
my_list1=input().split()
my_list2=input().split()
for i in my_list1:
    for j in my_list2:
        if i==j:
            a=i,j
            print(a,end=" ")