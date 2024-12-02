#in-class coding for Monday, December 2
# classes and object-oriented programming

class Dog:
   def __init__(self, name, age, breed, tricks):
       self.name = name
       self.age = age
       self.breed = breed
       self.tricks = tricks

   def learn_tricks(self,new_tricks):
       for i in range(len(new_tricks)):
           self.tricks.append(new_tricks[i])
   def print_values(self):
       print(self.name, self.age, self.breed, self.tricks)


    class Puppy(Dog):
        def __init__(self, name, age, breed, tricks):
     #Puppy is a subclass of Dog
     #Dog is the superclass of Puppy

if __name__ == "__main__":
    my_dog = Dog("Doug",9,["beagle","bulldog"],[])
    print(my_dog.name)
    my_dog.learn_tricks(["sit","down"])
    print(my_dog.tricks)
    her_dog = Dog("Bentley", 4, 'golden retriever',["sit","stay"])
    her_dog.print_values()



