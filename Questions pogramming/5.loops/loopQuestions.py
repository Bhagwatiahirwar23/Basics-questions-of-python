# Factorial
# 5! = 1*2*3*4*5

# for -----------------
'''x = 5
ans = 1
#     1,2,3,4,5
for i in range(1, 6):
    ans = ans*i

print(ans)'''


'''x = int(input("Enter the Value of X   "))
ans = 1
#     1,2,3,4,5
for i in range(1, x+1):
    ans = ans*i

print(ans)'''

# While ------------------
# home work

# Pattern of rectangle -------------
'''l = int(input("Enter the lenght of Rectangle"))
b = int(input("Enter the width of Rectangle"))'''

'''
* * * * *
* * * * *
* * * * *
'''
'''for i in range(b):
    print("* " * l)

print("---End---")'''

# Right Angled Triangle---------
'''
*      ----- 1
* * -------- 2
* * * ------ 3
* * * * ---- 4
'''
'''n = 4
for i in range(4):
    print("* " * (i+1))


n = int(input("Enter the side of Triangle"))
for i in range(n):
    print("* " * (i+1))'''


'''
1
2 2
3 3 3
4 4 4 4....
'''

'''n = int(input("Enter the side of Triangle"))
for i in range(n):
    print((str(i+1) + " ") * (i+1))'''

# rhombus
'''
__* * * *   -----4
_* * * *    ----3
__* * * *     ----2
_* * * *      ----1
'''

'''n = 4
for i in range(4):
    print(" " * (n-i) + "* " * n)'''


'''
__* * * * * * *   ----4
_* * * * * * *    ----3
__* * * * * * *     ----2
_* * * * * * *      ----1
'''



# list -------------------------------------------
# lst = [2, 4, 6, 8, 10]
# zero based
#      0  1  2  3  4
# print(lst)

# traverse
# list with for loop
'''for i in lst:
    print(i)'''


# indexing
'''print(lst[3])
print(lst[0])'''

'''for i in range(5):
    print(i, lst[i])'''

# properties of list

# 1. Hetro.....
'''lst1 = ["Vidhan", 43, 12.12, [1, 2, 3], 78]
print(lst1)
n = len(lst1)   # it gives length of list
print👎
for i in range(n):
    print(lst1[i])
    print(type(lst1[i]))'''


# 2 Ordered ---- it indexing
# 3. Changable   ---->  Mutable
lst = [1, 3, 5, 11]
# print(lst)
'''
lst[0] = 100
print(lst)'''

# Some imp methods of list


# 1. append() ---> add
'''lst.append(45)
print(lst)

lst.append("Shivi")
print(lst)'''

# 2. pop() --- we pass index here
'''lst.pop(0)
print(lst)'''

# 3. remove() --- we pass element
'''lst.remove(45)
print(lst)'''


# insert(index,element)  ---> add any element at any particular index
'''lst.insert(2, "Bhagwati")
print(lst)'''

# 4. clear()  --- to clear the list
'''lst.clear()
print(lst)'''

# 6. index()
'''ind = lst.index(11)
print(ind)'''

# 7. sort()
'''lst1 = [1, 12, 4, 2, 7, 100, 9]
print("Before sort")
print(lst1)

print("after sort")
lst1.sort()
print(lst1)'''


# -----------------------------Tuple ----------------------------
'''tup1 = (1,2,3,4,5)
print(tup1)
print(type(tup1))'''

# hetro......
'''tup2 = ("Ankna", 45, 123.123, [1,2,3])
print(tup2)'''
'''
for i in tup2:
    print(i)'''


# 2. Ordered
'''n = len(tup2)
print👎
for i in range(n):
    print(tup2[i])'''

#  3. NON changable ---> immutable  --> cant update, delete or add
# print(tup2[0])


# tup2[0] = "Litoriya"
# del tup2[0]
# tup2.append("Vidhan")
# tup1.clear()

# print(tup1)

# methods of tuple
# count()
'''t1 = (1,2,3,2,2,2,3,1,11,1,1,1)
print(t1)

c = t1.count(11)
print(c)
'''

# index()  --- return the index of that element
# print(t1.index(11))


# --------------------set----------------
'''l1 = [2,4,7,2,2]
s1 = {2,4,7,2,2}
print(s1)
print(l1)
print(type(s1))


# print(s1[0])
print(l1[0])

'''

# methods of set
# 1. add
'''s1 = {1,2,34,5}
print(s1)

s1.add(23)
print(s1)'''

# 2. remove()
'''s1.remove(5)
print(s1)'''

# 3. a.union(b)

'''a = {1,2,3,4}
b = {2,4,6,8}
print(a.union(b))'''

# 4. a.intersection(b) ------> common
# print(a.intersection(b))

# Write a program in Python to reverse a word
'''word = "Tajmahal"
newword = word[::-1]
print(newword)'''


'''lst = [1,2,3,4,5]
print(lst[4])'''


# colen : ---> sub list
'''print(lst[0:3])
print(lst[1:4])
print(lst[:])
print(lst[2:])
print(lst[::-1])'''


# Write a program that appends the square of each number to a new list.

input = [11, 3, 2, 4, 5]
# output = [121, 9, 4, 16, 25]
output = []
for i in input:
    output.append(i*i)

print(output)




# Write a Python program to count the number of even and odd numbers
input = [1, 2, 34, 5 , 6, 7, 8, 9, 34, 33, 12]
even_count = 0
odd_count = 0
for i in input:
    if i % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even Count", even_count)
print("Odd Count", odd_count)






# negetive index
'''lst = [1,2,12,122]
       # 0 1  2  3
    #   -4 -3 -2 -1

print(lst[3])
print(lst[-1])'''