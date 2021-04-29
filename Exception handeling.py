class CustomException(Exception):pass
class PrecedingNumberError(CustomException):pass
a = 0
try:
    num = int(input("Enter value: "))
    if num<a:
        raise PrecedingNumberError
    
    elif num>a:
        print("Value is Greater then zero. And the value is:", num)
    elif num==a:
        print("", num)

except PrecedingNumberError:
    print("Value is less then zero. And the value is:", num)