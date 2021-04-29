class Employee:
    _id=0
    _name=""
    _department=""
    _salary=0
	
    def setData(self,id,name,department,salary):
        self._id=input("Enter id: ")
        self._name = input("Enter name: ")
        self._department = input("Enter department: ")
        self._salary = input("Enter salary: ")
	
    def showData(self):
        print("Id\t:",self._id)
        print("Name\t:", self._name)
        print("Department:", self._department)
        print("Salary\t:", self._salary)

def main():
    emp=Employee()
    emp.setData(0, '1', '2', '3')
    emp.showData()
	
if __name__=="__main__":
    main()