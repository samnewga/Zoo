#################################################################################################
#Samael Newgate
#4/22/2018
#CSC102
#################################################################################################
#Add polymorphism to your parent and child classes (subclasses) by adding __str__ functions.
#The __str__ function should print the parent attributes as well as the unique child attributes.
#
#The makeNoise() function of the Animal class will need to be overridden in each subclass.
#The makeNoise function will need to print the sound the animal makes to the screen.
#
#All instantiated Animal objects should be stored in the Zoo list.
#Traverse the Zoo list using a loop and have each animal polymorphically print its attributes and call the makeNoise function. 
#
#Be sure to use comments for both structure of the program and documentation of the code.
#################################################################################################
class Animal: #Parent Class
    def __init__(self,atype,age,color): #intializer
        self.AnimalType = atype
        self.AnimalAge = age
        self.AnimalColor = color
    def makeNoise(self):    #method
        pass
    def __str__(self): #__str__ for print
        return "Animal type is {} age is {} color is {}".format(self.AnimalType,self.AnimalAge,self.AnimalColor,self.makeNoise())
    



class Cat(Animal): #Child Class Cat
    
    def __init__(self,atype,age,color,name,sound): #intilaizer of Cat Child
        Animal.__init__(self,atype,age,color)
        #unique Attributes
        self.myName = name 
        self.mySound = sound
    def __str__(self): #polymorphism for Cat child
        return Animal.__str__(self) +" I'm a {} and my sound is {}".format(self.myName,self.makeNoise())
    def makeNoise(self): #overriding for cat child
        return self.mySound
class Dog(Animal):
    
    def __init__(self,atype,age,color,name,sound):
        Animal.__init__(self,atype,age,color)
        #unique Attributes
        self.myName = name
        self.mySound = sound
    def __str__(self): #polymorphism for Dog child
        return Animal.__str__(self) +" I'm a {} and my sound is {}".format(self.myName,self.makeNoise())
    def makeNoise(self):    #overriding for dog child
        return self.mySound
    
class Parrot(Animal):
    
    def __init__(self,atype,age,color,name,sound):
        Animal.__init__(self,atype,age,color)
        #unique Attributes
        self.myName = name
        self.mySound = sound
    def __str__(self): #polymorphism for Parrot child
        return Animal.__str__(self) +" I'm a {} and my sound is {}".format(self.myName,self.makeNoise()) 

    def makeNoise(self):    #overriding for Parrot child
        return self.mySound
    
    
#instances   
cat1 = Cat("Mammal,","5,","black,","cat,","meoww.")
cat2 = Cat("Mammal,","2,","white,","cat,","meoww.")
dog1 = Dog("Mammal,","5,","black,","dog,","woff woff.")
dog2 = Dog("Mammal,","2,","white,","dog,","woff woff.")
parrot1 = Parrot("Mammal","5,","yellow and red,","parrot,","squawk.")
parrot2 = Parrot("Mammal","2,","green and blue,","parrot,","squawk.")
zoo = [cat1,dog1,parrot1,cat2,dog2,parrot2]

for i in zoo:
    print (i)
    
    


