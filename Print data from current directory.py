import os

#currentDirectory = os.getcwd()
#print(currentDirectory)
#os.chdir('C:\\Users\\Priyank\\Desktop\\Priyank\\Sem-8\\Artificial Intelligence')
currentDirectory = os.getcwd()
print(currentDirectory)
        
def files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file

for file in files("."):
    print (file)