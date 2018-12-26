class Animal:
    def catagory(self):
        print("catagorized as animal")
    def sounding(self):
        print("sounds like animal")

class Dog(Animal):
    def sounding(self):
        print("sounds like dog by overriding sounds of the Animal")



animal = Animal()
animal.catagory()
animal.sounding()


dog= Dog()
dog.catagory()
dog.sounding()


