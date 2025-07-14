student = {
    "name": "prem",
    "age": 20,
    "branch": "Computer Engineering",
}

print(student["name"])

# print(student.name)  
# Error
# because it is key-value pair , dot . is use for attributes
#if you wnt to use . 

from collections import namedtuple
Student = namedtuple("Student", ["name", "age", "branch"])
prem = Student(name="prem", age=20, branch="Computer Engineering")
print(prem.name)
print(prem.age)



student["collge"] = "sal"
print(student)

del student["branch"]
print(student)





for key in student:
    print(key, ":", student[key])


print(student.keys())
print(student.values())
print(student.items())


#set
colors = {"red", "green", "blue"}
colors.add("yellow")
colors.remove("green")

for color in colors:
    print(color)


student = {}

student["name"] = input("Enter your name: ")
student["age"] = int(input("Enter your age: "))
student["city"] = input("Enter your city: ")

print("\n--- Student Info ---")
for key, value in student.items():
    print(f"{key}: {value}")
