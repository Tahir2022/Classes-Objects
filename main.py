class Dog(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.li = [1, 3, 4]


    def speak(self):
        print("Hi I am", self.name, "and I am", self.age, "years old")

    def talk(self):
        print("Bark!")


# class Cat(object):
#    def __init__(self, name, age, color):
#        self.name = name
#        self.age = age
#        self.color = color

#    def speak(self):
#        print("Hi I am", self.name, "and I am", self.age, "years old")

class Cat(Dog):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def talk(self):
        print("Meow!")


tom = Cat('Tom',5, 'blue')
tom.speak()
tom.talk()