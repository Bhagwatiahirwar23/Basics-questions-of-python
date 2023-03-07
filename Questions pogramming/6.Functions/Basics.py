# Fuctions --------
'''
print("Bhagwati")
print("Happy New Year")

print("Ram")
print("Happy New Year")

print("Trapti")
print("Happy New Year")'''


'''def fun_name():
#     mycode'''

# Function define
def wish():
    print("Happy New Year")
    """Multiple lines"""

'''print("My funtion is runing")
# funtion call
wish()
print("My funtion is stop")'''

'''
print("Bhagwati")
wish()

print("Ram")
wish()

print("Trapti")
wish()
'''

# fuction define
'''def add():
    a = 10
    b = 100
    print(a+b)
'''
# function call
# add()

# types of fuction
# 1. take nothing return nothing
# fuction define
'''def add():
    a = 10
    b = 100
    print(a+b)'''

# function call
'''x = add()
print(x)'''

# take somethig return nothing

'''
# function define
def add(a, b):
    ans = a+b
    print(ans)

# function call
add(10, 20)
add(50, 70)


def multi(a, b):
    ans = a*b
    print(ans)


multi(10, 4)


def sub(a, b):
    print(a-b)

sub(10, 40)


def square(a):
    print(a*a)
    # print(a**2)

square(13)'''


# progra, to print a^b
'''def pow(a, b):
    print(a**b)

pow(2, 3)'''


# 3. take somthing return something

'''def add(a, b):
    ans = a+b
    return ans


result = add(10, 30)
print(result)


def good_eve(name):
    a = "Good Evening " + name
    # print(a)
    return a


x = input()
new = good_eve(x)
print(new)'''


# write a funtion which will return max of 2 number.
'''def mymax(a, b):
    if a > b:
        print("a is greater")
    else:
        print("b is greater")


x = int(input("Enter the value of first Number"))
y = int(input("Enter the value of second Number"))

mymax(x, y)'''
'''

def mymax2(a, b):
    if a > b:
        ans = a
    else:
        ans = b
    return ans


x = int(input("Enter the value of first Number"))
y = int(input("Enter the value of second Number"))

ans = mymax2(x, y)
print(ans)
'''

'''
def age(a):
    if a >= 18:
        ans = "You can Vote"
    else:
        ans = "You can't Vote"

    return ans


x = int(input("Enter Your Age"))
ans = age(x)
print(ans)
'''

'''x = int(input("Enter your age"))
if x >= 18:
    print("You can vote")
else:
    print("You can't Vote")
    
'''