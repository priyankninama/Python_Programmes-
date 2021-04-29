fname = input("Enter File name: ")

with open(fname, "r") as file:
	data = file.readlines()
	for line in data:
		word = line.split()
		print (word[2])

# python program to print initials of a name
# def name(s):

# 	l = s.split()
# 	new = ""

# 	for i in range(len(l)-1):
# 		s = l[i]
# 		new += (s[0].upper()+'.')

# 	new += l[-1].title()
	
# 	return new
			
# s =input("Enter your name: ")
# print(name(s))		
