              # MRO easy version
class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

print(D.__mro__)


                  # STATIC and CLASSIC method
class MyClass:
    @staticmethod
    def static_method():
        print("This is a static method")

MyClass.static_method()

class MyClass:
    @classmethod
    def class_method(self):
        print(f"This is a class method of {self.__name__}")
        # cls можно использовать для доступа к атрибутам класса

MyClass.class_method()

#  MRO+Mult.Inheritance+init_2x=code
class PC:
    def __init__(self):
        pass

    def power_on(self):
        print("Computer powered on")


class KB:
    def __init__(self):
        pass

    def connect(self):
        print("Keyboard connected")


class Monitor:
    def __init__(self):
        pass

    def display(self):
        print("Monitor displaying")


class Desktop(PC, KB, Monitor):
    def __init__(self):
        super().__init__()

    def start(self):
        self.power_on()
        self.connect()
        self.display()


desktop = Desktop()
desktop.start()

# INHERITANCE
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} says 'Hello!'")


class Dog(Animal):  # Dog наследует от Animal
    def __init__(self, name, breed):
        super().__init__(name)  # Вызываем конструктор базового класса
        self.breed = breed

    def bark(self):
        print(f"{self.name} the {self.breed} barks loudly")


my_dog = Dog("Bobik", "Avcharka")
my_dog.speak()
my_dog.bark()

# Mult. INHERITANCE
#
class A:
    def method(self):
        print("Method from A")


class B:
    def method(self):
        print("Method from B")


class C(B, A):  # Наследование от двух классов: A и B
    pass


my_object = C()
my_object.method()  # Выводит "Method from A"
