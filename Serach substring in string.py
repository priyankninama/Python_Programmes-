string = input("Enter String: ")
substring = input("Enter substring to match: ")

print("The original string is: " + string)

print("Substring is: " + str(substring))

res = [sub for sub in substring if sub in string]
  
string = ''.join(res)
print("Sub String Found : " + string)
