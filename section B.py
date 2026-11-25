# Section B Python Programming:-


#question 11 


# class Student:
#     def __init__(self, name, marks):
#         self.__name = name
#         self.__marks = marks

#     def display(self):
#         print("Name:", self.__name)
#         print("Marks:", self.__marks)

# s = Student("Sahil", 89)
# s.display()


#question 12 


# try:
#     with open("students.txt", "r") as file:
#         data = file.read()

#         lines = data.splitlines()
#         words = data.split()

#         print("Total Lines:", len(lines))
#         print("Total Words:", len(words))

# except FileNotFoundError:
#     print("Error: students.txt file not found!")