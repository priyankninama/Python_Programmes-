String = input("Enter string to sort: ")

words = String.lower()

def sortString(str):
    return ''.join(sorted(words))
word = (sortString(words))

print("Original String:", String)      
print("Alphabetically Sorted String: ", word)