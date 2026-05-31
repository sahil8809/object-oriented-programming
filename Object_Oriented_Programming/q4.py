# Parent class
class Animal:
    def __init__(self,name,colour,is_dangerous):
        self.name = name
        self.colour = colour
        self.is_dangerous = is_dangerous
        print("Animal makes sound")
        print("name of the Animal :",self.name)
        
        if self.is_dangerous == "yes":
            print(f"{self.name} is dangerous!")
        else:
            print(f"{self.name} is friendly!")


# Child class
class Dog(Animal):
    def bark(self):

        print("Dog is barking...")

name = input("Enter name of the animal :")
colour = input("Enter colour of the animal :")
is_dangerous = input("The animal is dangerous (YES/NO) :").lower()
print(90*"-")
# Object
d1 = Dog("Tomm","White",True)
d1.bark()   # child method
