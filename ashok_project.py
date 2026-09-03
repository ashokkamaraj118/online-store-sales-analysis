class collage:
    def _init_(self):
        self.student = {} # creating dict to store details

    #Adding students
    def stud_id(self,stud_id,name,dept,batch):
        if stud_id in self.student:
            print("student is already exist")
        else:
            self.student [stud_id] = { "name" : name , "dept" : dept , "batch" : batch}
            print("student added successfully")

#to update details of student

    def update_stud( self , stud_id , name = None , dept = None , batch = None):
     if stud_id in self.student:
        if name :
            self.student [stud_id]["name"] = name
        if dept :
            self.student [stud_id]["dept"] = dept
        if batch :
            self.student [stud_id]["batch"] = batch
            print("student details update successfully")
     else:
         print("stud_id not founded")

#to delete student details 

    def del_stud(self , stud_id):
        if stud_id in self.student:
            del self.student [stud_id]
            print(f"{stud_id} has deleted successfully")
        else:
            print(f"student id {stud_id} not founded")


 #to view particular 

    def view_stud (self , stud_id):
        if stud_id in self.student :
            print("student id :" , stud_id)
            print("name :" + self.student [stud_id]["name"])
            print(f"dept :{self.student [stud_id]["dept"]}")
            print("batch :" + self.student [stud_id]["batch"])
        else:
            print("stud_id not founded")


#to view all details 

    def view_all_stud(self):
        if self.student :
            for stud_id , i in self.student.items():
                print("student id :" + stud_id )
                print("name : " + i["name"])
                print("dept :" + i ["dept"])
                print("batch : " + str(i["batch"]))
                print("--"*20)
            else:
                print("no students founded")

#create object
def  main ():
    mng_sys = collage()

    #for infinite loop
    while True :
        print("1. add student")
        print("2. uodate student ")
        print("3. delete student")
        print("4. view particular student ")
        print("5. view all student")
        print("6. exit")

        choice = input("enter your choice : ")

        if choice =='1':
            stud2_id = input("enter student id : ")
            name = input ("enter name : ")
            dept = input ("enter the dept : ")
            batch = input ("enter the batch : ")
            mng_sys.add_stud(stud2_id , name , dept , batch )

        elif choice =='2':
            stud_id = input ("enter the stud id : ")
            name = input ("enter name (if no change ,press enter) : ")
            dept = input ("enter dept ,if no change ,pree enter : ")
            batch = input ("enter batch (if no change ,press enter) : ")
            mng_sys.update_stud(stud_id , name or None , dept or None , batch or None)

        elif choice == '3':
            stud_id = input("enter stud_id : ")
            mng_sys.del_stud(stud_id)

        elif choice == '4':
            stud_id = input("enter stud_id : ")
            mng_sys.view_stud(stud_id)

        elif choice =='5':
            mng_sys.view_all_stud()

        elif choice =='6':
            break

        else:
            print("invaild input , pleace try again ")

    main()     







