#Write a Python program to find common items in two lists.
my_list=input().split()
for i in range(0,len(my_list)-1,2):
    (my_list[i]),(my_list[i+1]) = (my_list[i+1]),(my_list[i])
print(my_list)