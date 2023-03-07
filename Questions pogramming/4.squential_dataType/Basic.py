'''list
tuple
set
dictionary
String 
list vs tuple'''

'''lst = [2,4,6,8,10]'''
# zero based indexing
'''for i in lst:
    print(i)'''

'''for i in range(5):
     print(i,lst[i])'''

'''tpl = (1,4,3,2,6)
for i in tpl:
    print(i)'''

'''for i in range(5):
     print(i,tpl[i])'''

# list - append ,pop,remove,insert,index ,clear , sorted
# append - it is used for add the value in the end
'''lst = [1,2,4,5,3]
print("before",lst)
lst.append(34)
print("After",lst)'''

# 2.pop - pop used for remove the last element of the list , and it is use for remove element - element value
'''lst = [1,2,4,5,3]
print("before",lst)
lst.pop()
print("After",lst)
lst.pop(3)
print("after mention element index", lst)'''

# 3.remove - use element
'''lst = [1,2,4,5,3]
lst.remove(2)
print(lst)'''

#  4. insert - list_name.insert(index_pos,element)
'''lst = [1,2,4,5,3]
lst.insert(2,67)
print(lst)'''

# 5. clear - it clear all element of the list
'''lst = [1,2,4,5,3]
lst.clear()
print(lst)'''

# 6. sort - we can sort the list in ascending or descending order
'''lst = [1,9,4,5,3]
lst.sort()
print(lst)'''

# properties - mutable(changeable),allow duplicate value , hydrogenous , ordered , use square bracket
# 1.mutable- we can modify the list like , insert  , update , sort ,remove , clear
'''lst = [1,2,4,5,3]
lst.append(6)
lst.pop()
lst.insert(2,89)
lst.remove(5)
lst.clear()
lst.sort()
print(lst)
'''
# 2.allow duplicate value
'''lst = [1,2,4,5,3,2,2,3]
print(lst)'''

# 3.hydrogenous - it is used for store different datatype in a list
'''lst = ["siya", 45,5.7]
print(lst)'''

# 4. ordered - accept indexing
'''lst = ["siya", 45,5.7]
print(lst[0])'''

# tuple - count, index
# 1. count - it is use for count duplicate value in  a tuple
'''tpl = (1,2,3,4,5,3,2)
c= tpl.count(3)
print(c)
'''
# 2.index- it show the index of element in  a tuple ,
'''tpl = (1,2,3,4,5,3,2)
c= tpl.index(5)
print(c)'''

# properties - unmutable(unchangeable), updation not allow
# 1. updation not allow- we can not modify the list like , insert  , update , sort ,remove , clear
'''tpl = (1,2,4,5,3)
tpl.append(6)
tpl.pop()
tpl.insert(2,89)
tpl.remove(5)
tpl.clear()
tpl.sort()'''

# set - add , remove,union , intersection
'''st = {2,3,5,8}
print(st)'''

# add
'''st.add(7)
print(st)'''

# remove
'''st.remove(8)  #use element not a index number
print(st)'''

# union
'''a = {1,3,4,5,2,1}
b = {3,46,9,7,4}
print(a.union(b))'''

# intersaction
'''print(a.intersection(b))'''

# properties - unordered , duplicate value not allow , hydroponic
# 1.not allow duplicate value
'''st = {1,2,4,5,3,2,2,3}
print(st)'''

# 2.hydrogenous - it is used for store different datatype in a list
'''st = {"siya", 45,5.7}
print(st)
'''
# 2. unordered - not accept indexing
'''st = {"siya", 45,5.7}
print(st[1])
'''
# 2 write a program that appends the square of each number to a new list
'''lis = [23,5,4,1]
new_lis = []
for i in range(len(lis)):
    sqr = i ** 2
    print(sqr)
    new_lis.append(sqr)
print(new_lis)'''