def file_read(fname):
    with open(fname,"w")as myfile:
        string = input("Enter String To Append: ")
        myfile.write(string)
        myfile.write('\n')
#myfile.write("This is my Python programme \n")
    txt = open(fname)
    print(txt.read())
file_read('file.txt')
