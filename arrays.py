courses = ["math","science","english"]
print(courses)
#on accessing an element in an array
print(courses[2])

#looping through an array
for a in courses:
    print("course is",a)

#adding a new element into an array
courses.append("Laravel")
print(courses)

#deleting an element from an array
courses.remove("math")
print(courses)

