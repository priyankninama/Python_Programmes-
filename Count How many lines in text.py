fname = input("Enter File name: ")
lines = 0
with open (fname, 'r') as f:
    for line in f:
        lines +=1
print("Number of lines: ", lines)


count = {}
for word in open(fname).read().split():
    if word in count:
        count[word] += 1
    else:
        count[word] = 1
print(count)