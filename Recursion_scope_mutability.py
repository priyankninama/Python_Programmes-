import argparse

ap = argparse.ArgumentParser()
ap.add_argument("--input",type=int, help="The input Number", default=5)
args = vars(ap.parse_args())

print("----Recursion----")
def factorial(n):
    if n == 1:
        return 1
    else:
        return n*(factorial(n-1))
print("Factorial of ",args['input'] , ":",factorial(args['input']))

print("\n----Function Scoping----")
a = 10
if a == 10:
    print("Num1 :",a)
    b = a + 2
print("Num2 :",b)
print("B is in the Scope")
def print_fun():
    c = a + b    
    print("Num3 :", c)
try:
    print("Num3 :", c)
except:
    print("C is out of Scope")
print_fun()

print("\n----List Mutablity----")

lis = ["Computer", "IT", "EC", "IC"]
print("Inital List: \n", lis)

lis.append("Civil")
print("After Appending: \n",lis)

lis.pop()
lis.pop()
print("After Popping: \n",lis)

