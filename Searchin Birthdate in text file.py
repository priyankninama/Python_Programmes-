import re 
fin = open("student.txt","r")  
text = fin.read() 
match=re.search(r'(\d+/\d+/\d+)',text) 
print (match.group())
print(text) 