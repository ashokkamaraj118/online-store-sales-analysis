
# a = input("enter the name : ")
# b = input("enter the age : ")
# print("my name is:",a)
# print("my age is :",b)



# a = int(input())
# b = int(input())
# c = int(input())
# d = a*b*c
# f = a+b+c
# e = d/f
# print(e)


name = (input())
score = int(input ())
department = input ()
org_score = score/10
print(name)
print(org_score)
print(department)




class Bikers:
    def _init_(self):
        self.bike_id = {} # creating dict to store details

    def add_bike(self,name,bike_id,org_score,dept):
            self.bike [add_bike] = { "name" : bike_id , "dept" : org_score , "batch" : dept} # type: ignore
            print("Bikes detailas added successfully")

    #Adding bike model
    def add_bike1(self,bike_model,name,year,price,model):
        if bike_model in self.bike:
            print("model is already exist")
        else:
            self.bike[bike_model]={"company":name,"bike_model":model,"year":year,"price":price}
        print("bike added successfully")
    #To update details of bikes
    def update_bike_id(self,bike_id,name=None,bike_model=None,year=None,price=None):
        if bike_model  in self.bike:
            if name:
                self.bike[bike_id]["name"]=name
            if bike_model:
                self.bike[bike_id]["bike_model"]=bike_model
            if year:
                self.bike[bike_id]["year"]=year
            print("bike details updated successfully")
        else:
            print("bike ID not found")
    #To delete bike details
    def del_bike(self,bike_id):
        if bike_id in self.bike:
            del self.bike[bike_id]
            print(f"{bike_id}has been deleted successfully")
        else:
            print(f"bike ID{bike_id} not found")
    #To view particular empolyee details
    def view_bike(self,bike_id):
        if bike_id in self.bike:
            print("BIKE_ID:", bike_id)
            print("Name: "+self.bike[bike_id]["name"])
            print(f"Year: {self.bike[bike_id] ["year"]} ")       
        else:
            print("No bike found")

#    TO view all details
    def view_bike(self):
        if self.bike:
            for bike_id, i in self.bike.items():
                print("BIKE_ID: ",bike_id)
                print("Name:",i["name"])
                print("Year:",i["year"])
                print("--"*20)
        else:
            print("no bike_id found") 
#creating obj:
def main():
    mng_sys = Bikers()
    #for infinite loop 
    while True :
        print()
        print()
        print()
        choice=input ("enter your choice:")


        if choice == '1':
            bike_id=input("enter bike_id:")
            name=input("enter user name :")
            org_score=input("enter org_score")
            dept=input("enter dep details")
            mng_sys.add_bike(bike_id,org_score,dept)
        elif choice == '2':
            bike_id=input("enter bike_id:")
            name=input("enter  name (if no change,press enter):")
            year=input("enter year(if no change ,leave blank): ")
            mng_sys.update_bike_id(bike_id or None,name or None ,year or None ,) 
        

        elif choice == '3':
            bike_id = input("enter the bike_id:")
            mng_sys.del_bike(bike_id)

        elif choice == '4':
            bike_id=input("bike_id")
            mng_sys.view_bike()

        elif choice == '5':
            break

        else:
            print("invaild input , please try again!,pls choose only between 1 and 6")
main()