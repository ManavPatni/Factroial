#Created by Manav Patni
#Program to find factorial of any number

num = int(input("Enter any number here:- "))
n = num
fact = 1
while num >= 1:
    fact = fact * num
    num = num - 1
print("Factorial of", n, "is", fact)
