'''x = input() # it always take input in str format
print(type(x))

y = 12.5
print(type(y))'''

# OPerator
# a + b
# 2+3

# Arithmetic
# +,-,,/,//,%,*


# 1. +

'''x = 10
y = 5
z = 2.75'''

'''name = "Bhagwati"
last = "Ahirwar"
'''
'''print(x+y)'''
# print(name +last)

# 2. -
'''print(x-y)'''
# print(name-last) unsupported operand type(s) for -: 'str' and 'str


# 3. *
'''print(x*y) #50
print("hello " * 10)'''
# print("hello" * "world")  # can't multiply sequence by non-int of type 'str'


# 4. /
# x = 10, y = 5
'''print(x/y)  #--> 2
print(y/x)  #--> 0.5

print(10//2)
print(10/2)

# 5 //
print(12//5) # --> 2.4 but ans = 2
print(14//5) # --> 2,8 but ans = 2'''


# 6 % --> remainder

'''print(13 % 5)
print(50 % 11)'''

'''a = 15
b = 2
print(a % b)
print(13 % 2) # --> 1

print(15 % 3)'''


'''print(12 % 10) # --> 2
print(13 % 2)  # --> 1
print(5 % 3)   # --> 2
print(24 % 7)  # --> 3
print(32 % 9)  # --> 5'''


#  7 **  power
'''print(2 ** 4)  # --> 2^4 = 2*2*2*2 --> 16
print(3 ** 2)'''

# Questions
'''
print(12 ** 1)
print(4 ** 2)
print(6 ** 3)
print(1 ** 5)
print(2 ** 5)'''

# Question
'''print(12 * 5)
print(12 + 5)
print(12 - 5)
print(12 // 5)
print(12 / 5)
print(12 % 5)'''


# Relational operator ------------------------------------------------
# ==
# >
# <
# >=
# <=
# !=
# they return true or false


# 1 == (equal to)
'''a = 10
b = 20
print(a == b)

a = 10
b = 10
print(a == b)'''

# 2 >
'''a = 20
b = 10
print(a > b)'''

# 3. <

'''a = 20
b = 10
print(a < b)'''

# 4. >=

'''a = 20
b = 20
print(a >= b)'''


# 5. <=

'''a = 20
b = 200
print(a <= b)'''


# 6. != not equal

'''a = 20
b = 20
print(a != b)'''


# Questions
'''a = 13
b = 29
print(a > b)
print(a < b)
print(a == b)
print(a >= b)
print(a <= b)
print(type(a != b))
'''

# Logical operators --------------------------------------------------
# and
# or
# not

a = 5
b = 10
'''print((a < b) and (a != b))

print((a < b) or (a == b))

print(not (a == b))
#           False   --> True'''


'''print(a != b)  # --> True
print(not (a != b))
#           true   --> False'''


# Question
'''a = 50
b = 70
# ----False-------True   ans = True
ans = (a >= b) or (a != b)
print(ans)

# ----True ------- True --- ans = True
ans = (a <= b) or (a != b)
print(ans)

# -----False ----- False -- ans False
ans = (a >= b) or (a == b)
print(ans)

# ----False-------True   ans = False
ans = (a >= b) and (a != b)
print(ans)

# ----True - ------ True --- ans = True
ans = (a <= b) and (a != b)
print(ans)

ans = (a >= b) and (a == b)
print(ans)

#  ----- False -- ans = True
ans = not(a == b)
print(ans)'''

# -------False --- ans = True
'''ans = not(a > b)
print(ans)'''


# Assignment operator ---------------------------------------------------

# 1. =
'''x = 100
y = x
print👍

name = "Vidhan"
student = name
print(student)
'''
# += ---> a += b ---> a = a + b
'''a = 10
b = 50'''
# a = a + b  # a+=b
'''a += b
print(a, b)

x = 7
y = 10

# y = y + x
y += x
print(y)'''

# 3. -=  ---- a -= b ---> a = a - b
'''x = 100
y = 30

x -= y   # x = x - y
print(x)'''

# 4. *=  ---- a *= b ---> a = a * b

'''x = 100
y = 30

x *= y   # x = x * y
print(x)
x = 3000
y = 30
x *= y  # ---> 3000 * 30 = 90000
print(x)
'''

# 5. /= ---- a /= b --> a = a / b
'''a = 100
b = 50
a /= b  # a = a / b
print(a)'''


# 6. %= ---  a%=b ---- a = a % b
'''a = 12
b = 5

a %= b
print(a)'''


# 7. //=

'''a = 100
b = 50
a //= b  # a = a // b
print(a)'''


# Bitwise -------------------------------------------
# & --- bitwise and
# | ---> Bitwise or
# ~ ---> Bitwise not

# bit level
# 0, 1
# 10 in bin ----> 1010
# 6 =             0110
# and  -----------0010
# or -------------1110
a = 10
b = 6
print(a & b)
print(a | b) # ---> 14
print(~a)
print(~b)