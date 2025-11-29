# # Write a program that stores 5 employee details and prints only employees with skill Python.
# employee = {
#         "employee1":{
#         "id":101,
#         "name":"tarun",
#         "skills":["python","c"]
#         },
#     "employee2":{
#         "id":102,
#         "name":"rohit",
#         "skills":["python","c","java"]
#     },
#     "employee3":{
#         "id":103,
#         "name":"ravi",
#         "skills":["java","c"]
#     },
#     "employee4":{
#         "id":104,
#         "name":"raju",
#         "skills":["php","c"]
#     },
#     "employee5":{
#         "id":105,
#         "name":"rakesh",
#         "skills":["react","c"]
#     }

# }
# # for emp in employee.values():
# #     if "python" in emp["skills"]:
# #         print(emp["name"])

# # task2:Write a program to display:
# # Total number of employees
# # Employees who know more than 2 skills
# count=0
# for emp in employee.values():
#     count=count+1
#     if emp["skills"].length>2:
#         print(emp["name"])
# print(count)

# task3---------------------
# Print employee name and skills only if:
# They know Python
# And they are active (add is_active: True/False)

employees = {
    "employee1": {
        "id": 101,
        "name":"tarun",
        "skills": ["python","c"],
        "is_active": True
    },
    "employee2": {
        "id": 102,
        "name":"rohit",
        "skills": ["python","c"],
        "is_active": True
    },
    "employee3": {
        "id": 103,
        "name":"ravi",
        "skills": ["react","c"],
        "is_active": False
    },
    "employee4": {
        "id": 104,
        "name":"tarun",
        "skills": ["java","c"],
        "is_active": False
    }
    
}

# for emp in employees.values():
#     if "python" in emp["skills"] and emp["is_active"]==True:
#         print(f"{emp['id']}-{emp['name']}-{emp['skills']}")

# task-4-------
# Create a function filter_python_employees() that:

# takes employees dictionary as a parameter

# filters Python-skilled active employees

# returns a list of matching employee names

# prints the returned value
# def filter_python_employees(employee):
#     names=[]
#     for emp in employee.values():
#         if "python" in emp['skills'] and emp['is_active']==True:
#             names.append(emp['name'])
#     return names
# nameList=filter_python_employees(employees)
# print(nameList)

# name=input("enter your name:")
# age=int(input("Enter your age:"))
# language=input("enter your favorite language:")
# print(f"hell0 {name}! You are {age} years old and love {language}")

a=20
b=30
c=40
print(a+b+c,(a+b+c)/3,a*b*c)













