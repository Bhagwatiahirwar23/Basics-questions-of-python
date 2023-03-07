# if - Syntax

# if(expression):

'''a = input()
b = input()
if (a==b):
    print("equal")
print("end")'''

'''a = input()
b = input()
if (a!=b):
    print("not equal")
print("end")'''

'''a = input()
b = input()
if (a==b):
    print("equal")
else:
    print("Not equal")
print("end")'''

'''a = int(input("Enter the value of a\n"))
b = int(input("enter the value of b\n"))
if (a>b):
    print("A")
elif (a==b):
    print("equal")
else:
    print("B")
print("end")
'''
'''a = int(input("Enter the value of a\n"))
b = int(input("enter the value of b\n"))
if (a>b):
    print("a is greater")
elif (a==b):
    print("a and b both are equal")
else:
    print("b is greater")
print("end")'''

'''a = float(input("Enter the value of a\n"))
b = float(input("enter the value of b\n"))
if (a>b):
    print("a is greater")
elif (a==b):
    print("a and b both are equal")
else:
    print("b is greater")
print("end")'''

# 1. check wether the number is even or odd
'''num = int(input("Enter the number\n"))

if (num % 2) == 0:
    print("even")
else:
    print("number is odd")
print("end")'''
#
# 2.check wether the number is positive or negative

'''num = int(input("Enter a number:\n "))
if num > 0:
   print("number is Positive ")
elif(num==0):
    print("Zero")
else:
   print("number is Negative ")'''

# 3. Sum of two number using take the input from user

'''a = int(input("Enter the number a\n "))
b = int(input("Enter the number b\n"))
c = a+b
print("sum of a and b is ",c)
'''
# 4. check weather the nu ber is minimum or maximum
'''a = int(input("enter the  number a\n"))
b = int(input("enter the number b\n"))
minimum = min(a,b)
print("minimum number is ",minimum)'''
#
# another way
'''a = 34
b = 57
if (a<b):
    print("minimum")
elif (a==b):
    print("both are equal")
else:
    print("maximum")
print("end")'''

'''a = int(input("enter the  number a\n"))
b = int(input("enter the number b\n"))
maximum = max(a,b)
print("minimum number is ",maximum)'''

# 6. Check weather a number is divisible by 5 and 11 or not
'''num = int(input("enter the number\n"))

if((num % 5==0) & (num % 11==0)):
    print("Number is divisible by 5 and 11")
else:
    print("Number is not divisible by 5 and 11")'''

# 7. Check whether the triangle is equlateral , scalene or isosceles.
'''A = int(input("Enter the value a\n"))
B = int(input("Enter the value b\n"))
C = int(input("Enter the value c\n"))
if A==B==C:
    print("Equlateral")
elif A==B or B==C or C==A:
    print("Isosceles")
else:
    print("Scalene")'''
#
# 8. Check whether the char is vowel or consotants.
'''# char = input("Enter a char:\n")
# if (char == 'a' or char== 'e' or char=='i' or char=='o' or char=='u'):
#     print("Vowel")
# else:
#     print("Consonant")
'''
# Another way
'''char = input("Enter a char:\n")
vowels = "aeiou"
if char in vowels:
    print("Vowel")
else:
    print("Consonant")'''

# # 9.Check whether the triangle is valid or not if angles are given.
'''A = 45
B=  45
C = 90
Triangle = A+B+C
if Triangle==180:
    print("Triangle is valid")
else:
    print("Triangle is not valid")'''

# Another way
'''A = int(input("Enter the angle A\n"))
B=  int(input("Enter the angle B\n"))
C = int(input("Enter the angle C\n"))

if A+B+C==180 and  A>0 and B>0 and C>0:
    print("Triangle is valid")
else:
    print("Triangle is not valid")'''

# 10 Enter the student marks and find percentage and grade
'''student_marks = int(input("Enter the student marks\n"))
total_marks = 100
student_Persantage=student_marks//total_marks
resultant = student_Persantage*100
if student_marks >90 :
    print("Student grade is A+\n")
elif student_marks<90 or student_marks>80:
    print("Student grade is A\n")
elif student_marks<80 or student_marks>60:
    print("Student grade is B\n")
elif student_marks<60 or student_marks>50:
    print("Student grade is C\n")
elif student_marks<50 or student_marks>=33:
    print("student grade is D\n")
else:
    print("student is fail")
'''

# 10. Enter the student marks and find percentage and grade
'''Hindi = int(input("Enter the student marks of hindi\n"))
English = int(input("Enter the student marks of english\n"))
maths = int(input("Enter the student marks of maths\n"))
physics = int(input("Enter the student marks of physics\n"))
chemistry = int(input("Enter the student marks of chemistry\n"))

total_marks = Hindi+English+maths+physics+chemistry
Average = total_marks/5
if Average >90 :
    print("Student grade is A+\n""Student persantage is",Average,"%")
elif Average<90 or Average>80:
    print("Student grade is A\n""Student persantage is", Average, "%")

elif Average<80 or Average>=75:
    print("Student grade is B\n""Student persantage is", Average, "%")
elif Average<75 or Average>=50:
    print("Student grade is C\n""Student persantage is", Average, "%")
elif Average<50 or Average>=33:
    print("Student grade is A+\n""Student persantage is", Average, "%")
else:
    print("student is fail","Student persantage is ","%")'''

# 11. Read the age of candidate and determine whether it is eligible for vote
'''Age = int(input("Enter a candidate age\n:"))
if Age>=18:
    print("Candidate is eligible for vote!")
else:
    print("Candidate is not eligible for vote!")'''
#
# 12. Calculate profit and loss on a transaction
'''selling_price = int(input("Enter a selling price\n"))
cost_price = int(input("Enter a cost price\n"))
# profit = selling_price - cost_price
# loss = cost_price-selling_price

if selling_price>cost_price:
    print("profit")
elif selling_price==cost_price:
    print("No profit no loss")
else:
    print("loss")
'''

