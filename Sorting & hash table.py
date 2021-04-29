import random

numbers = [1,4,3,8,16,15,25,46,28,66,54,75,98,23,42]
new = sorted(numbers)
print('Unsorted Number :', numbers)
print('\nSorted Number :',new)
num = int(input('\nEnter a Number to Search in list: '))
flag = True
index = 0
for temp in new:
    if temp == num:
        print('Number Exist at Index ', index)
        flag = False
    index = index + 1
if flag:
    print('Number does not Exist in the List')
hash_table = {}
while True:
    new_data = input("\nEnter a data to generate Hash : ")
    if 'break' in new_data.lower():
        break
    new_key = len(new_data)
    new_key = ( random.randrange(100) + new_key ) + new_key * new_key
    hash_table[str(new_key)] = new_data
print(hash_table)
