#built in functions/ stnadard library functions

y = max(99,23,45,89,72,23,14,54)
print("the max vaue is",y)

x = min(99,23,45,89,72,23,14,54)
print("the min vaue is",x)

# user defined functions
def name():
    print("Rumplestilskin")
name() #calling a function

def multiply():
    x = 38
    q = 75
    print(x*q)
multiply()

#parameters/variable and arguments/value
def add(a,b):
    print(a+b)
add(4,7)

def employee(name,gender,age,position,salary):
    print(name,gender,age,position,salary)
employee("Chiri","female","55","CEO","50k")
employee("Chiri","female","55","CEO","50k")
employee("Chiri","female","55","CEO","50k")
employee("Chiri","female","55","CEO","50k")



#A programme that displays details of 5 student
# 2 use a user defined function with the help of parameter and arguments


def studentdet(fullname, age, course, gender):
    print(fullname,age,course,gender)
studentdet("Alexandiah Michael","16","Medicine","Female")
studentdet("jeremy Diego","26","Biochemistry","Male")
studentdet("Mac Miller","23","Law","Male")
studentdet("Blessing Mufasa","22","History","Female")



