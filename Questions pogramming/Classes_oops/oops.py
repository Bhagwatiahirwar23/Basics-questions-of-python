class student():
    pass
s1 = student()
l = list()
print(type(s1))
print(type(l))

s2 = student()
s3 = student()
# print(s2,s3)
s1.name = 'bhagwati'
s1.rollNumber= 34

s2.name = 'ishika'
s2.rollNumber= 34

s3.name = 'khushi'
s3.rollNumber= 34

print(s2.name)

print(s1.__dict__)
print(s2.__dict__)

print(hasattr(s1, 'name'))
print(getattr(s1, 'name'))
print(getattr(s1, 'name',' '))
print(delattr(s1, 'name'))
print(s1.__dict__)