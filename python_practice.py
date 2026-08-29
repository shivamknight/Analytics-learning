# BAsic understanding questions





# 1. Write a function that checks whether a given number is even or odd.
# user=int(input("Enter a Number: "))
# print(user)
# if(user>0):
#     if(user%2!=0):
#         print(f"{user} is ODD")
#     else:
#         print(f"{user} is EVEN")
# else:
#     print("Enter number greator than 0....")






#2. Write a function that returns the largest number among three given integers.

# x=int(input("Enter 1st number: "))
# y=int(input("Enter 2nd number: "))
# z=int(input("Enter 3rd number: "))
# print(f"entered numbers are {x},{y} and {z}")
# # if(x>=y and x>=z):
# #     print(f"{x} is greator than both {y} and {z}")
# # elif(y>= x and y>=z):
# #     print(f"{y} is greator than both {x} and {z}")
# # else:
# #     print(f" {z} is greator than both {x} and {y}")

# larget=max(x,y,z)
# print(larget)

    




# 3. write a program to reverse the digits of a given integer.
# x=int(input("enter a number: "))
# original_num=x
# rev_num=0
# while x>0:
#     last_digit=x%10
#     rev_num=(rev_num*10)+ last_digit
#     x=x//10
# print(f"Given number: {original_num}")
# print(f"Reversed number: {rev_num}")





# 4. write a function which checks whether a number is palindrome.

# num=int(input("Enter a number: "))
# check = num
# rev_num=0
# while num>0:
#     last_digit=num%10
#     rev_num=(rev_num*10)+last_digit
#     num=num//10
# if (rev_num==check):
#     print(f"{check} is PALINDROME")
# else:
#     print(f"{check} is NOT PALINDROME")






# write a program to find the factorial of a number using iteration(for OR while loops).

# def factorial(x):
#     if(x==0 or x==1):
#         return 1
#     else:
#         temp=x*factorial(x-1)
#         return temp
# num=int(input("enter a number: "))
# print(factorial(num))
# this uses recursion----------------------------------
# def factorial(x):
#     if(x==0 or x==1):
#         return 1
#     result =1
#     for i in range(2,x+1):
#         result=result*i
#     return result
# num =int(input("Enter a number: "))
# print(factorial(num))
# this uses the for loop with iteration method----------
# def factorial(x):
#     result=1
#     while(x>1):
#         result=result*x
#         x=x-1
#     return result
# num=int(input("Enter a number: "))
# print(factorial(num))
# ///this is also iteration method using while loop------




# write a fuction that count the number of digits in a given number:

# def count(x):
#     digit=len(str(abs(x)))
#     return f"total length of numbers entered: {digit}"


# num=int(input("Enter any number: "))
# print(count(num))




# write a function that finds the sum of digits in a given number


# def sumdom(x):
#     temp=0
#     for i in x:
#         i=int(i)
#         temp=temp+i
#     return f"total sum of  all digits: {temp}"
    
# num=str(input("enter the number: "))
# print(sumdom(num))


#========================================================================================================================
# Arrays in python:-------------------------
# what is array?  
#     :=> An array is the collection of the values in a single data type

# positive indexing 
# print(arr[0])
# print(arr[1])

# negative indexing
# print(arr[-1])
# print(arr[-2])
 
# modfying elements:
# arr[0]=100
# print(arr)

# accessing array
# for i  in range(len(arr)):
#     print(arr[i])


# taking input in array


# arr=list(map(int,input("enter the numbers: ").split()))
# arr=[5,4,2,9,8,6,7,1,3]


# arr.sort(reverse=True)
# print(arr)





    

# write a function to find whether a number is prime or not.

# def isprime(x):
#     if x<=1 or x==2:
#         return False
#     for i in range(3,int(x**0.5)+1):
#         if x%i==0:
#             return False
#     return True
# num=int(input("enter a number: "))
# # print(isprime(num))
# if isprime(num):
#     print("is the prime")
# else:
#     print("is not prime")



# def isprime(x):
#     if x>2:
#         for i in range(3,x-1):
#             if x%i==0:
#                 return f"{x} is not prime number."
#         else:
#             return f"{x} is prime number."
            
#     elif x==2:
#         return f"{x} is  even prime number."
#     else:
#         return f" {x} is not prime number."
# num=int(input("Enter a number: "))
# print(isprime(num))





# write a function to find the maximum element from the array
# def maximum(x):
#     x.sort()
#     temp=x[len(arr)-1]
#     return f"{temp}"
# arr=[50,30,10,20,40]
# print(maximum(arr))


# write a fucntion find a minimum element in an array
# def mini(x):
#     x.sort(reverse="True")
#     temp=x[-1]
#     return f"{temp}"
# arr=[50,30,10,20,40]
# print(mini(arr))





# write a function to check whether a string is plaindrome or not.
 
# def palindrom(x):
#     if x==x[::-1]:
#         return True
#     else:
#         return False

# name=list(map(str,input("enter a name:").strip()))
# # print(palindrom(name))
# if palindrom(name):
#     print(f"Given STRING is Palindrome")
# else:
#     print(f"Given STRING is NOT Palindrome")
    






# write a function to count vowels in string
# def count(word):
#     vovel="aeiou"
#     cout=0
#     for i in vovel:
#         if i in word.lower():
#             cout+=1

#     return cout
# name="Shivam"
# print(count(name))




# write a function to merge two sorted array into one sorted array

# def merger(arr1,arr2):
#     for i in arr2:
#         arr1.append(i)
#     arr1.sort()
#     return arr1
# x=list(map(int,input("enter the numbers: ").split(",")))
# y=list(map(int,input("enter the numbers: ").split(",")))
# print(merger(x,y))






# write a function to find the second largest number in an Array.

# def maxima(x):
#     x=list(set(x))
#     if len(x) < 2:
#         return f"Minimum 2 numbers are required.."
#     x.sort(reverse=True)
#     return x[1]
# arr=list(map(int,input("Enter a number: ").replace(","," ").split()))
# print(maxima(arr))



# Beginner
# Print all elements of a list.
# Find the sum of all elements.
# Find the largest element.
# Find the smallest element.
# Count even numbers.
# Count odd numbers.
# Calculate average of elements.
# Search for a given element.


# Find the sum of all elements.
# arr=[1,2,3,4]
# temp=0
# for i in arr:
#     temp=temp+i
# print(temp)

# Find the largest element.
# first way
# arr=[1,5,4,7,6,8,3]
# print(max(arr))
# second way
# arr=[1,5,4,7,6,8,3]
# arr.sort()
# print(arr[-1])

# Find the smallest element.
# first way
# arr=[1,5,4,7,6,8,3]
# print(min(arr))
# second way
# arr=[1,5,4,7,6,8,3]
# arr.sort()
# print(arr[0])


# Count even numbers.
# arr=[1,5,4,7,6,8,3,10,12,14,19,51,12,16,41,75,95,84,48,76,57,23]
# temp=0
# for i in arr:
#     if(i%2==1):
#         temp+=1
# print(temp)

# Count odd numbers.
# arr=[1,5,4,7,6,8,3,10,12,14,19,51,12,16,41,75,95,84,48,76,57,23,21]
# temp=0
# for i in arr:
#     if(i%2==1):
#         temp+=1
# print(temp)




# Calculate average of elements.
# arr=[1,5,4,7,6,8,3,10,12,14,19,51,12,16,41,75,95,84,48,76,57,23,21]
# count=sum(i for i in arr )/len(arr)
# print(count)


# Search for a given element.
# arr=[1,5,4,7,6,8,3,10,12,14,19,51,12,16,41,75,95,84,48,76,57,23,21]
# target=int(input("Enter your clg id: "))

# def check(x,y):
#     for i in y:
#         if (i==x):
#             return f"You are eligible for the exams"
#     return "You are not eligible for the exams"
# print(check(target,arr))
# ___________________________________________________
# ---------------------------------------------------|
# hard and intermediate questions from leetcode:-----|
# ---------------------------------------------------|
# ___________________________________________________|


# Q1. write a function to find two numbers in an array whose sum equals a target value
# arr=[0,1,4,5,6,3,9,8,7,2,10]
# target=int(input("enter the targeted Sum: "))
# def find(x,y):
#     for i in range(len(y)):
#         for j in range(i+1,len(y)):
#             if arr[i]+arr[j]==x:
#                 print(f"{arr[i]}+{arr[j]}={x}")
# find(target,arr)




# Q2. write a function to move all zeroes in an array to the end while maitaining order



