#Kieren Singh Gill
#09/14/2020
#Python Fall 2020, Section 1
#GillKieren_assign1_problem2.py

#Prompt the user to input three names and store them in separate variables.
name1 = input("Please enter name #1: ")
name2 = input("Please enter name #2: ")
name3 = input("Please enter name #3: ")

#Print an empty line
print()

#Print the names in every possible order.
#Use the + to concatenate names with commas or other symbols for formatting sake.
print("Here are your names in every possible order:")
print("--------------------------------------------")
print()
print("1.", name1 + ",", name2 + ",", name3)
print()
print("2.", "*" + name1 + "*", "*" + name3 + "*", "*" + name2 + "*")
print()
print("3.", name2 + "-" + name1 + "-" + name3)
print()
print("4.", name2)
print(name3)
print(name1)
print()
print("5.", name3)
print("  ", name2)
print("  ", name1)
print()
print("6.", name3)
print("--", name1,sep="-")
print("--", name2,sep="-")
