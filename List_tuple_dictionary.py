tup = ("Computer", "IT", "IC", "EC")
student = ["120", "70", "80", "60"]

print("\nThe Tuples are", tup)
print("\nThe List is", student)
print("\nLets Make a dictionary with Branch and student intake: ")

dic = {}

for (Branch,Students) in zip(tup,student):
    dic[Branch] = Students
print("\nThe dictonary is", dic)


