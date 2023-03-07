# function - function is a block of code which utilize again and again  by call it
# types of function
# 1. Take nothing return nothing(TNRN)
# 2. Take something return nothing(TSRN)
# 3. take something return somthing(TSRS)

# syntax
# def func_name():
    # mycode
# -------------------------------------------------add------------------------------------------------------------------
# 1. add two numbers TNRN
'''def add():
    a = 8
    b = 9
    ans = a+b
    print(ans)
add()'''

# 2. add two numbers TSRN
'''def add(a , b):
    ans = a+b
    print(ans)
add(4,6)'''

# direct
'''def add(a , b):
    print(a+b)
add(4,6)'''

# 3. Add two numbers (TSRS)
'''def add(a , b):
    ans = a+b
    return ans
x = add(4,6)
print(x)'''

# another
# Add two numbers(take the input from the user) (TSRS)
'''def add(a , b):
    ans = a+b
    return ans
n1 = int(input("Enter the value of n1\n"))
n2 = int(input("Enter the value of n1\n"))
x = add(n1 , n2)
print(x)'''


# ----------------------------------------count Even--------------------------------------------------------------------
# without take input from the user(TSRS)
'''def count_even(lst):
    ans = 0
    for i in lst:
        if i%2==0:
            ans = ans+1
    return ans
l = [2,6,3,4,9,8]
C = count_even(l)
print(C)'''

# take input from the user(TSRS)
'''def count_odd(lst):
    ans = 0
    for i in lst:
        if i%2!=0:
            ans = ans+1
    return ans
l = list(map(input().split()))
C = count_odd(l)
print(C)'''
# ----------------------------------------count odd--------------------------------------------------------------------
# without take input from the user(TSRS)
'''def count_odd(lst):
    ans = 0
    for i in lst:
        if i%2!=0:
            ans = ans+1
    return ans
l = [2,6,7,3,9,8]
C = count_odd(l)
print(C)'''

# take input from the user(TSRS)
'''def count_odd(lst):
    ans = 0
    for i in lst:
        if i%2!=0:
            ans = ans+1
    return ans
l = list(map(int , input("Enter the value of list\n").split()))
C = count_odd(l)
print(C)'''

# ----------------------------------------sum of  Even number --------------------------------------------------------------------
# # without take input from the user(TSRS)
'''def sm_even(lst):
    ans = 0
    for i in lst:
        if i%2==0:
            ans = ans+i
    return ans
l = [2,6,3,4,9,8]
C = sm_even(l)
print(C)'''

# take input from the user(TSRS)
'''def sum_even(lst):
    ans = 0
    for i in lst:
        if i%2==0:
            ans = ans+i
    return ans
l = list(map(int , input("Enter the value of list\n").split()))
C = sum_even(l)
print(C)'''

# ----------------------------------------Even number --------------------------------------------------------------------
# # without take input from the user(TSRN)

'''def num_even(lst):
    ans = 0
    for i in lst:
        if i%2==0:
            print(i)
l = [2,6,3,4,9,8]
num_even(l)'''

# take input
'''def num_even(lst):
    ans = 0
    for i in lst:
        if i%2==0:
            print(i)
l = list(map(int,input("Enter values").split()))
num_even(l)'''
# --------------------------------------??????----------------------------------------------------------------------------
# TSRS
# # Pending
'''def num_even(lst):
    ans = []
    for i in lst:
        if i%2==0:
            ans.append(i)
    return ans
l = [2,6,3,4,9,8]
C = num_even(l)
print(C)
'''
# ----------------------------------------Factorial---------------------------------------------------------------------
# 1, (Take input from the user) - TSRS
'''def fact(n):
    ans = 1
    for i in range(1, n+1):
        ans = ans*i
    return ans
x = int(input("Enter any value :\n"))
ans = fact(x)
print("factorial of",x,"is" , ans)
'''
# without take input from the user -  (TSRS)
'''def fact(n):
    ans = 1
    for i in range(1, n+1):
        ans = ans*i
    return ans
x = 8
ans = fact(x)
print("factorial of",x,"is" , ans)'''

# 2, TSRN
'''def fact(n):
    ans = 1
    for i in range(1, n+1):
        ans = ans*i
    print(ans)
x = int(input("Enter any value :\n"))
fact(x)'''

# ------------------------------------------multiply list---------------------------------------------------------------
# 1. Multiply list - (take something retrun somthing) - user input()
'''def mul(lst):
    ans = 1
    for i in lst:
        ans = ans * i
    return ans
l = list(map(int , input("enter values in list").split()))
result = mul(l)
print(result)'''

# Multiply list - (take something retrun somthing) - without user input()
'''def mul(lst):
    ans = 1
    for i in lst:
        ans = ans * i
    return ans
l = [2,4,6,7]
result = mul(l)
print(result)'''


# 1. Multiply list - (take something retrun nothing) - user input()
'''def mul(lst):
    ans = 1
    for i in lst:
        ans = ans * i
    print(ans)
l = list(map(int , input("enter values in list").split()))
mul(l)
'''
# --------------------------------write a program sum of numbers (in list)TSRN------------------------------------------

'''def sm(numbers):
    num_sum = 0
    for i in numbers:
        num_sum = num_sum+i
        print(num_sum)
    # avg_sum = num_sum//numbers
        # print(avg_sum)

n = list(map(int, input("Enter numbers ").split()))
sm(n)'''

# --------------------------------write a program sum of numbers (in list)TSRS------------------------------------------

'''def sm(numbers):
    num_sum = 0
    for i in numbers:
        num_sum = num_sum+i
    return num_sum

n = list(map(int, input("Enter numbers ").split()))
result = sm(n)
print(result)'''

# --------------------Write a program you can vote or not. (with user input)(TSRS)-----------------------------------
'''def Age(a):
    if a>= 18:
        ans="You can vote"
    else:
        ans = "you cant vote"

    return ans

n= int(input("Enter your age"))
ans = Age(n)
print(ans)'''

#------------------------ Write a program you can vote or not. (without user input)(TSRN)-------------------------------
'''def Age(a):
    if a>= 18:
        print("You can vote")
    else:
        print("you cant vote")
Age(67)'''

# def pelin(n):
#     for i in range(n):
#     # s = str(input(s))
#         s = input(" ")
#         if s == s[::-1]:
#             print('YES')
#         else:
#             print('NO')
# n1 = input()
# ans =pelin(n1)
# print(ans)

# cook your dish here

def zoogame(n):
    for x  in range(n):
        for y in range(n):
            ans = x*(3*y)
    return ans

m = input()
r = zoogame(m)
print(r)
