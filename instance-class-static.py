

class Myclass:
    def instance_method(self):  #object level
        print("instance method")


    @classmethod
    def class_method(cls):  #class level
        print("class method")

    @staticmethod
    def static_method(): #this will not come under the class and object
        print("static method")

obj = Myclass()
obj.instance_method()
Myclass.class_method()
Myclass.static_method()



#Class Level example --> we can overwite and we can change

class empolyee:
    company_name = "Open AI"

    @classmethod
    def change_company(cls,new_name):
        cls.company_name = new_name

empolyee.change_company("Microsoft")
print("Class Method Output: ",empolyee.company_name)



#Static Method --. it will not depend on class and object it is a helper utility

class Math:

    @staticmethod
    def add(a,b):
        return a+b
print("Static Method Output: ", Math.add(1,2))