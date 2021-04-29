a = int(input("Enter value of a:"))    
b = int(input("Enter value of b:")) 

try:     
    c = a/b 
    print("Not Zero") 
except ArithmeticError:  
    print("Can't divide with zero")  