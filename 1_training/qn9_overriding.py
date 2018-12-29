#!/usr/bin/env python3.7


class Animal:
    def catagory(self):
        print("catagorized as animal")
    def sounding(self):
        print("sounds like animal")

class Dog(Animal):
    def sounding(self):
        print("sounds like dog by overriding sounds of the Animal")


if __name__ == "__main__":

    animal = Animal()
    animal.catagory()
    animal.sounding()


    dog= Dog()
    dog.catagory()
    dog.sounding()


